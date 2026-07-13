"use client"

import * as React from "react"
import { cn } from "@/lib/utils"
import Link from "next/link"

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: "default" | "outline" | "ghost" | "link" | "glow"
  size?: "sm" | "md" | "lg" | "xl"
  href?: string
}

const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant = "default", size = "md", href, children, ...props }, ref) => {
    const base = "inline-flex items-center justify-center font-medium transition-all focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 rounded-lg"
    
    const variants = {
      default: "bg-primary text-primary-foreground hover:bg-primary/90 shadow-md",
      outline: "border border-border bg-background hover:bg-accent hover:text-accent-foreground",
      ghost: "hover:bg-accent hover:text-accent-foreground",
      link: "text-primary underline-offset-4 hover:underline",
      glow: "bg-primary text-primary-foreground shadow-lg glow-primary hover:shadow-xl hover:scale-[1.02] transition-all",
    }
    
    const sizes = {
      sm: "h-8 px-3 text-sm",
      md: "h-10 px-4 py-2 text-sm",
      lg: "h-12 px-6 text-base",
      xl: "h-14 px-8 text-lg",
    }
    
    if (href) {
      return (
        <Link
          href={href}
          className={cn(base, variants[variant], sizes[size], className)}
        >
          {children}
        </Link>
      )
    }
    
    return (
      <button
        ref={ref}
        className={cn(base, variants[variant], sizes[size], className)}
        {...props}
      >
        {children}
      </button>
    )
  }
)
Button.displayName = "Button"

export { Button }
