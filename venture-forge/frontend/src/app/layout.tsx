import type { Metadata } from "next"
import "./globals.css"
import { Navbar } from "@/components/ui/navbar"
import { Footer } from "@/components/ui/footer"

export const metadata: Metadata = {
  title: "VentureForge — AI Startup Engine",
  description: "Discover market opportunities, validate ideas, generate MVPs, and launch startups with AI.",
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-background antialiased">
        <Navbar />
        <main className="min-h-[calc(100vh-16rem)]">{children}</main>
        <Footer />
      </body>
    </html>
  )
}
