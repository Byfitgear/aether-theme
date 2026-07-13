"use client"

import { useState } from "react"
import { Card, CardContent, CardHeader, CardTitle, CardDescription, CardFooter } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"

const PLANS = [
  {
    name: "Free",
    price: "$0",
    period: "/month",
    description: "Explore and discover opportunities",
    features: [
      "5 market scans per month",
      "Basic opportunity scoring",
      "MVP plan generation (1)",
      "Community access",
      "Dashboard with basic metrics",
    ],
    cta: "Get Started",
    highlighted: false,
  },
  {
    name: "Pro",
    price: "$49",
    period: "/month",
    description: "Build and launch your startup",
    features: [
      "Unlimited market scans",
      "Deep AI opportunity analysis",
      "Full MVP code generation",
      "Deploy to Vercel (1 click)",
      "Advanced dashboard & analytics",
      "Stripe integration templates",
      "Priority support",
    ],
    cta: "Start Pro Trial",
    highlighted: true,
  },
  {
    name: "Enterprise",
    price: "$199",
    period: "/month",
    description: "Scale multiple products",
    features: [
      "Everything in Pro",
      "Multi-project workspace",
      "Custom AI agent training",
      "API access",
      "Team collaboration (up to 10)",
      "White-label deployment",
      "Dedicated account manager",
    ],
    cta: "Contact Sales",
    highlighted: false,
  },
]

export default function PricingPage() {
  const [annual, setAnnual] = useState(false)

  return (
    <div className="px-4 py-12 sm:px-6 lg:px-8">
      <div className="mx-auto max-w-6xl">
        {/* Header */}
        <div className="mb-12 text-center">
          <h1 className="text-3xl font-bold sm:text-4xl">Simple, Transparent Pricing</h1>
          <p className="mt-3 text-lg text-muted-foreground">
            Start free. Upgrade when you're ready to build.
          </p>

          {/* Toggle */}
          <div className="mt-6 inline-flex items-center gap-3 rounded-full bg-muted p-1">
            <button
              onClick={() => setAnnual(false)}
              className={`rounded-full px-4 py-1.5 text-sm font-medium transition-all ${!annual ? "bg-primary text-primary-foreground shadow-sm" : "text-muted-foreground"}`}
            >
              Monthly
            </button>
            <button
              onClick={() => setAnnual(true)}
              className={`rounded-full px-4 py-1.5 text-sm font-medium transition-all ${annual ? "bg-primary text-primary-foreground shadow-sm" : "text-muted-foreground"}`}
            >
              Annual <Badge variant="success" className="ml-1 text-xs">-20%</Badge>
            </button>
          </div>
        </div>

        {/* Plans Grid */}
        <div className="grid gap-6 md:grid-cols-3">
          {PLANS.map((plan) => (
            <Card
              key={plan.name}
              className={`relative flex flex-col ${
                plan.highlighted
                  ? "border-primary/50 shadow-lg scale-[1.02]"
                  : "border-border/60"
              }`}
            >
              {plan.highlighted && (
                <div className="absolute -top-3 left-0 right-0 flex justify-center">
                  <Badge variant="default" className="px-4 py-1">Most Popular</Badge>
                </div>
              )}
              <CardHeader>
                <CardTitle>{plan.name}</CardTitle>
                <CardDescription>{plan.description}</CardDescription>
              </CardHeader>
              <CardContent className="flex-1">
                <div className="mb-6">
                  <span className="text-4xl font-bold">{plan.price}</span>
                  <span className="text-muted-foreground">{plan.period}</span>
                </div>
                <ul className="space-y-3">
                  {plan.features.map((feature) => (
                    <li key={feature} className="flex items-start gap-2 text-sm">
                      <span className="mt-0.5 text-green-500">✓</span>
                      <span className="text-muted-foreground">{feature}</span>
                    </li>
                  ))}
                </ul>
              </CardContent>
              <CardFooter>
                <Button
                  variant={plan.highlighted ? "glow" : "outline"}
                  className="w-full"
                  size="lg"
                >
                  {plan.cta}
                </Button>
              </CardFooter>
            </Card>
          ))}
        </div>

        {/* FAQ */}
        <div className="mx-auto mt-20 max-w-2xl text-center">
          <h2 className="text-2xl font-bold">Frequently Asked Questions</h2>
          <div className="mt-8 space-y-4 text-left text-sm text-muted-foreground">
            <div>
              <p className="font-medium text-foreground">Can I cancel anytime?</p>
              <p>Yes. Cancel your subscription at any time. No hidden fees.</p>
            </div>
            <div>
              <p className="font-medium text-foreground">Is there a free trial?</p>
              <p>The Pro plan includes a 14-day free trial. No credit card required.</p>
            </div>
            <div>
              <p className="font-medium text-foreground">What happens to my projects if I downgrade?</p>
              <p>Your generated projects remain accessible. You just lose scan credits.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
