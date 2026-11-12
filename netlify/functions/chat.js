const https = require('https');

const SYSTEM_PROMPT = `You are the {PlAIceholder} assistant — helpful, concise, and direct.

{PlAIceholder} designs, builds, and installs custom AI agents for companies with 10–200 employees. We handle one specific repeatable task your team does weekly, inside the tools you already pay for.

AGENT CATALOG:
Sales: Signal Prospector ($6,000 setup / $750/mo) | Inbound Lead Researcher ($3,500/$450/mo) | CRM Hygiene ($1,500/$250/mo) | Deal Follow-up Drafter ($3,500/$450/mo) | Meeting Prep Briefs ($1,500/$250/mo)
Customer success: Renewal Risk Radar ($3,500/$450/mo) | Support Ticket Triage ($1,500/$250/mo) | Customer Onboarding Tracker ($1,500/$250/mo)
Back office: Invoice Checker ($3,500/$450/mo) | Resume Screener ($3,500/$450/mo) | Weekly KPI Writer ($1,500/$250/mo)
Marketing: Competitor Watch ($1,500/$250/mo) | RFP and Questionnaire Drafter ($6,000/$750/mo)
We also build fully custom agents for tasks not on this list.

PRICING:
Starter: $1,500 setup + $250/mo care | Standard: $3,500 setup + $450/mo care | Advanced: $6,000 setup + $750/mo care
Every build includes a pilot on 20 real records before full deployment.

PROCESS (~2 weeks):
Free 30-min call → Fixed-price proposal → 1-hour discovery interview → Build + pilot on 20 records → Measure results + hand over

FOUNDING CLIENT DEAL:
20% off setup + 3 months care free, in exchange for publishing real measured results as a case study. Limited spots.

SAFETY (every agent):
Pilot first. Every AI finding cites its source. Spending caps before every run. No auto-deletes. Humans approve all actions. Full audit log.

TO BOOK A CALL: direct them to plaiceholder.io/contact.html

GUIDELINES:
- Keep replies under 120 words unless more detail is genuinely needed
- If someone describes a task, say which agent fits and what tier
- If they ask about pricing, give the tier table
- If they want to book, send them to the contact page
- Never guarantee specific ROI figures
- If unsure, say to reach out via the contact page`;

exports.handler = async function(event) {
  if (event.httpMethod === 'OPTIONS') {
    return {
      statusCode: 200,
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'POST, OPTIONS'
      },
      body: ''
    };
  }

  if (event.httpMethod !== 'POST') {
    return { statusCode: 405, body: 'Method not allowed' };
  }

  const apiKey = process.env.ANTHROPIC_API_KEY;
  if (!apiKey) {
    return { statusCode: 500, body: JSON.stringify({ error: 'API key not configured' }) };
  }

  let messages;
  try {
    ({ messages } = JSON.parse(event.body));
  } catch {
    return { statusCode: 400, body: JSON.stringify({ error: 'Invalid JSON' }) };
  }

  const payload = JSON.stringify({
    model: 'claude-haiku-5-5',
    max_tokens: 400,
    system: SYSTEM_PROMPT,
    messages: messages.slice(-10)
  });

  return new Promise((resolve) => {
    const req = https.request({
      hostname: 'api.anthropic.com',
      path: '/v1/messages',
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': apiKey,
        'anthropic-version': '2023-06-01',
        'Content-Length': Buffer.byteLength(payload)
      }
    }, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        try {
          const result = JSON.parse(data);
          resolve({
            statusCode: 200,
            headers: {
              'Content-Type': 'application/json',
              'Access-Control-Allow-Origin': '*'
            },
            body: JSON.stringify({ reply: result.content[0].text })
          });
        } catch (e) {
          resolve({ statusCode: 500, body: JSON.stringify({ error: 'Parse error' }) });
        }
      });
    });
    req.on('error', (e) => {
      resolve({ statusCode: 500, body: JSON.stringify({ error: e.message }) });
    });
    req.write(payload);
    req.end();
  });
};
