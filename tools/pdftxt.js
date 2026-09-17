const fs = require('fs');
const { PDFParse } = require('pdf-parse');
(async () => {
  const parser = new PDFParse({ data: new Uint8Array(fs.readFileSync(process.argv[2])) });
  const res = await parser.getText();
  process.stdout.write(res.text);
  await parser.destroy();
})().catch(e => { console.error('ERR', e.message); process.exit(1); });
