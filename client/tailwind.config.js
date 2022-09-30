/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,tsx}"],
  mode: 'jit',
  prefix: 'tw-',
    theme: {
      screens: {
        sm: '480px',
        md: '768px',
        lg: '976px',
        xl: '1440px'
      },
      extend: {
        maxWidth: {
          70: '70%',
        },
        height: {
          "content" : "max-content"
        },
        width: {
            '500': '500px',
            "content" : "max-content"
        },
        colors: {
          primary: '#2a77ff',
          lightGrey: '#f3f2f6',
          primaryDark: '#25316D',
          // primaryLight: "#25316D"
        },
        fontFamily: {
          'montserrat': ['Montserrat'],
        }
      }
    }
}