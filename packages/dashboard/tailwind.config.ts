import type { Config } from 'tailwindcss'
import { react } from '@openui-org/react'

export default {
  content: [
    './index.html',
    './src/**/*.{js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {},
  },
  plugins: [react],
} satisfies Config
