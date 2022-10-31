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
        backgroundcolor: "#EBD7C1",
      },
      dropShadow: {
        'accentgreen': '0 35px 35px rgb(140, 255, 152, 0.25)',
      },
    },
  },
  plugins: [],
}