import puppeteer from 'puppeteer';

async function generatePdfFromHtml(htmlContent: string, pdfPath: string) {
    // Launch a new browser instance
    const browser = await puppeteer.launch({ headless: true });
    
    // Open a new page
    const page = await browser.newPage();
    
    // Set the content of the page
    await page.setContent(htmlContent, { waitUntil: 'load' });
    
    // Generate the PDF from the page content
    await page.pdf({ path: pdfPath, format: 'A4' });
    
    // Close the browser
    await browser.close();
}

// Example usage
const htmlContent = `
    <html>
    <body>
        <h1>Hello, World!</h1>
        <p>This is a PDF generated from HTML content using Puppeteer.</p>
    </body>
    </html>
`;

const pdfPath = 'output.pdf';

generatePdfFromHtml(htmlContent, pdfPath)
    .then(() => console.log('PDF generated successfully!'))
    .catch(err => console.error('Error generating PDF:', err));
