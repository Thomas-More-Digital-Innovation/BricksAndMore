/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./voting/templates/voting/*.html",
    "./voting/templates/voting/components/*.html",
  ],
  theme:
  {
    extend: {
      colors: {
        bamBlue: '#151535',
        bamRed: '#d61523',
        bamDarkText: '#242424',
        bamText: '#807b77',
      },
      scale: {
        '200': '2.00',
      }
    }
  },
  plugins: [],
}