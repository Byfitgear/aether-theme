"use client"

import { useState } from "react"
import Link from "next/link"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"

export default function LoginPage() {
  const [email, setEmail] = useState("")
  const [loading, setLoading] = useState(false)

  const handleLogin = async () => {
    setLoading(true)
    // Simulate Clerk auth redirect
    await new Promise((r) => setTimeout(r, 1000))
    setLoading(false)
    alert("In production, this redirects to Clerk Auth.")
  }

  return (
    <div className="flex min-h-[calc(100vh-12rem)] items-center justify-center px-4 py-12">
      <Card className="w-full max-w-md">
        <CardHeader className="text-center">
          <CardTitle className="text-2xl gradient-hero bg-clip-text text-transparent">
            Welcome to VentureForge
          </CardTitle>
          <CardDescription>Sign in to start building your next startup</CardDescription>
        </CardHeader>
        <CardContent className="space-y-4">
          {/* Email Login */}
          <div className="space-y-2">
            <Input
              type="email"
              placeholder="Enter your email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
            <Button variant="glow" className="w-full" onClick={handleLogin} disabled={loading}>
              {loading ? "Signing in..." : "Continue with Email"}
            </Button>
          </div>

          {/* Divider */}
          <div className="relative">
            <div className="absolute inset-0 flex items-center"><span className="w-full border-t" /></div>
            <div className="relative flex justify-center text-xs uppercase"><span className="bg-background px-2 text-muted-foreground">Or continue with</span></div>
          </div>

          {/* Social Buttons */}
          <div className="grid grid-cols-2 gap-3">
            <Button variant="outline" className="w-full">Google</Button>
            <Button variant="outline" className="w-full">GitHub</Button>
          </div>

          <p className="text-center text-xs text-muted-foreground">
            By continuing, you agree to our{" "}
            <Link href="#" className="underline hover:text-foreground">Terms</Link>
            {" "}and{" "}
            <Link href="#" className="underline hover:text-foreground">Privacy Policy</Link>
          </p>
        </CardContent>
      </Card>
    </div>
  )
}
