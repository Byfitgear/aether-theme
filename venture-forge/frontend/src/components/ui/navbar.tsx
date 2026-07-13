"use client"

import Link from "next/link"
import { cn } from "@/lib/utils"
import { Button } from "./button"

export function Navbar() {
  return (
    <nav className="sticky top-0 z-50 w-full border-b border-border/40 bg-background/80 backdrop-blur-md">
      <div className="mx-auto flex h-16 max-w-7xl items-center justify-between px-4 sm:px-6 lg:px-8">
        {/* Logo */}
        <Link href="/" className="flex items-center gap-2">
          <span className="text-2xl font-bold gradient-hero bg-clip-text text-transparent">
            ⚡ VentureForge
          </span>
        </Link>

        {/* Nav Links */}
        <div className="hidden md:flex items-center gap-8">
          <NavLink href="/discover">Discover</NavLink>
          <NavLink href="/dashboard">Dashboard</NavLink>
          <NavLink href="/pricing">Pricing</NavLink>
        </div>

        {/* Auth Buttons */}
        <div className="flex items-center gap-3">
          <Button variant="ghost" size="sm" asChild>
            <Link href="/login">Sign In</Link>
          </Button>
          <Button variant="glow" size="sm" asChild>
            <Link href="/login">Get Started Free</Link>
          </Button>
        </div>
      </div>
    </nav>
  )
}

function NavLink({ href, children }: { href: string; children: React.ReactNode }) {
  return (
    <Link
      href={href}
      className="text-sm font-medium text-muted-foreground transition-colors hover:text-foreground"
    >
      {children}
    </Link>
  )
}
