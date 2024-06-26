import type { Metadata } from 'next'
import { ViewTransitions } from 'next-view-transitions'
import { Toaster } from 'sonner'
import './globals.css'

export const metadata: Metadata = {
  title: 'Home',
  description: 'Generated by create next app',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <ViewTransitions>
      <html lang="en" className="light">
        <body>
          <Toaster />
          {children}
        </body>
      </html>
    </ViewTransitions>
  )
}
