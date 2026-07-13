import Link from "next/link"
import { Button } from "@/components/ui/button"
import { Card, CardContent } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"

export default function HomePage() {
  return (
    <div className="flex flex-col">
      {/* Hero */}
      <section className="relative overflow-hidden px-4 py-24 sm:py-32 lg:px-8">
        <div className="absolute inset-0 gradient-hero opacity-5 blur-3xl" />
        
        <div className="relative mx-auto max-w-4xl text-center">
          <Badge variant="outline" className="mb-6">
            🚀 AI-Powered Startup Engine
          </Badge>
          <h1 className="text-4xl font-extrabold tracking-tight sm:text-6xl lg:text-7xl">
            From Idea to{" "}
            <span className="gradient-hero bg-clip-text text-transparent">
              Revenue
            </span>{" "}
            in 48 Hours
          </h1>
          <p className="mx-auto mt-6 max-w-2xl text-lg text-muted-foreground">
            VentureForge discovers market opportunities, validates demand with data, 
            generates your MVP code, and deploys it — all powered by AI agents working together.
          </p>
          <div className="mt-10 flex items-center justify-center gap-4">
            <Button variant="glow" size="xl" href="/discover">Start Building Free</Button>
            <Button variant="outline" size="lg" href="/pricing">View Pricing</Button>
          </div>
        </div>
      </section>

      {/* How It Works */}
      <section className="px-4 py-20 sm:py-28 lg:px-8">
        <div className="mx-auto max-w-6xl">
          <h2 className="text-center text-3xl font-bold sm:text-4xl">
            How VentureForge Works
          </h2>
          <p className="mx-auto mt-4 max-w-2xl text-center text-muted-foreground">
            Four AI agents. One unified engine. Your next startup.
          </p>
          
          <div className="mt-16 grid gap-8 sm:grid-cols-2 lg:grid-cols-4">
            {[
              { step: "01", icon: "🔍", title: "Discover", desc: "AI scans Reddit, HN, Product Hunt & more to find high-signal pain points" },
              { step: "02", icon: "📊", title: "Validate", desc: "Opportunity scorer evaluates TAM, competition, AI advantage & profitability" },
              { step: "03", icon: "⚙️", title: "Generate", desc: "MVP generator creates full project structure, database schema & API design" },
              { step: "04", icon: "🚀", title: "Launch", desc: "Deploy to production with one click. Track metrics. Iterate with AI." },
            ].map((item) => (
              <Card key={item.step} className="border-border/60 bg-card/50 backdrop-blur">
                <CardContent className="pt-6 text-center">
                  <div className="text-4xl mb-4">{item.icon}</div>
                  <Badge variant="outline" className="mb-3">{item.step}</Badge>
                  <h3 className="text-xl font-semibold mb-2">{item.title}</h3>
                  <p className="text-sm text-muted-foreground">{item.desc}</p>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* Stats */}
      <section className="px-4 py-16 lg:px-8">
        <div className="mx-auto max-w-6xl">
          <div className="rounded-2xl border border-border/60 bg-gradient-to-br from-primary/5 to-purple-500/5 p-8 sm:p-12">
            <div className="grid gap-8 sm:grid-cols-3 text-center">
              {[
                { value: "48h", label: "Average time to MVP" },
                { value: "94/100", label: "Top opportunity score" },
                { value: "$47B", label: "Total addressable market" },
              ].map((stat) => (
                <div key={stat.label}>
                  <div className="text-4xl font-bold gradient-hero bg-clip-text text-transparent">{stat.value}</div>
                  <div className="mt-2 text-sm text-muted-foreground">{stat.label}</div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="px-4 py-20 sm:py-28 lg:px-8">
        <div className="mx-auto max-w-3xl text-center">
          <h2 className="text-3xl font-bold sm:text-4xl">
            Ready to Build Your Next Startup?
          </h2>
          <p className="mt-4 text-lg text-muted-foreground">
            Join thousands of founders using VentureForge to go from idea to revenue faster than ever.
          </p>
          <div className="mt-8">
            <Button variant="glow" size="xl" href="/discover">Get Started — It's Free</Button>
          </div>
        </div>
      </section>
    </div>
  )
}
