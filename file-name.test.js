
/**
 * @jest-environment jsdom
 */

const { test, expect } = require("@jest/globals");
const {} = require("../document");

beforeAll(() => {
    let fs = require("fs");
    let fileContents = fs.readFileSync("bookings.html", "utf-8");
    document.open();
    document.write(fileContents);
    document.close();
});

