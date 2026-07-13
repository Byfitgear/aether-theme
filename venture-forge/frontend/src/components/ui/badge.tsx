import * as React from "react"
import { cn } from "@/lib/utils"

interface BadgeProps extends React.HTMLAttributes<HTMLDivElement> {
  variant?: "default" | "success" | "warning" | "destructive" | "outline"
}

const Badge = React.forwardRef<HTMLDivElement, BadgeProps>(
  ({ className, variant = "default", ...props }, ref) => {
    const variants = {
      default: "bg-primary/10 text-primary border-primary/20",
      success: "bg-green-500/10 text-green-600 border-green-500/20 dark:text-green-400",
      warning: "bg-yellow-500/10 text-yellow-600 border-yellow-500/20 dark:text-yellow-400",
      destructive: "bg-red-500/10 text-red-600 border-red-500/20 dark:text-red-400",
      outline: "text-foreground border-border",
    }
    return (
      <div ref={ref} className={cn("inline-flex items-center rounded-full border px-2.5 py-0.5 text-xs font-semibold transition-colors", variants[variant], className)} {...props} />
    )
  }
)
Badge.displayName = "Badge"

export { Badge }
