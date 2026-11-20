import { readFile } from 'node:fs/promises';

const token = process.env.APIFY_TOKEN;
if (!token) throw new Error('Set APIFY_TOKEN first.');
const headers = { Authorization: `Bearer ${token}`, 'Content-Type': 'application/json' };
const base = 'https://api.apify.com/v2';
const input = await readFile(new URL('../../data/sample-input.json', import.meta.url), 'utf8');
// Reconcile an ambiguous POST in Apify Console before starting another run.
const start = await fetch(`${base}/acts/datascraperes~gelbe-seiten-business-directory/runs?waitForFinish=60&timeout=90&maxTotalChargeUsd=0.05`, {
  method: 'POST', headers, body: input, redirect: 'error', signal: AbortSignal.timeout(100_000),
});
if (!start.ok) throw new Error(`Start request returned HTTP ${start.status}`);
const { data: run } = await start.json();
if (run.status !== 'SUCCEEDED') throw new Error(`Inspect run ${run.id} in Apify Console: ${run.status}`);
const dataset = await fetch(`${base}/datasets/${encodeURIComponent(run.defaultDatasetId)}/items`, {
  headers, signal: AbortSignal.timeout(30_000),
});
if (!dataset.ok) throw new Error(`Dataset request returned HTTP ${dataset.status}`);
console.log(JSON.stringify(await dataset.json(), null, 2));
