"use client"

import { useState } from "react"
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"

// Mock data simulating AI agent output
const MOCK_OPPORTUNITIES = [
  {
    id: "1",
    title: "AI-Powered Customer Support for E-commerce",
    description: "High volume of repetitive customer queries across Shopify stores. Current solutions are expensive ($200+/mo) or require heavy manual setup.",
    source: "reddit r/startups",
    score: 92,
    tam: "$12B",
    sam: "$2.4B",
    som: "$120M",
    growth: "+35% YoY",
    competition: "Low-Medium",
    tags: ["SaaS", "AI", "E-commerce"],
    status: "validated",
  },
  {
    id: "2",
    title: "Automated Compliance Checking for Fintech Startups",
    description: "Fintech founders spend 40+ hours/month on compliance documentation. Manual process leads to costly mistakes and delayed launches.",
    source: "hackernews",
    score: 88,
    tam: "$8B",
    sam: "$1.6B",
    som: "$80M",
    growth: "+28% YoY",
    competition: "Medium",
    tags: ["B2B", "Compliance", "AI"],
    status: "validated",
  },
  {
    id: "3",
    title: "Real-Time Sentiment Analysis for SaaS Products",
    description: "SaaS teams need instant feedback on user sentiment but existing tools are slow and expensive. Slack/Discord communities are underserved.",
    source: "producthunt",
    score: 85,
    tam: "$5B",
    sam: "$1B",
    som: "$50M",
    growth: "+42% YoY",
    competition: "Low",
    tags: ["Analytics", "AI", "Community"],
    status: "validated",
  },
  {
    id: "4",
    title: "Smart Contract Audit Assistant for Web3 Builders",
    description: "Web3 developers struggle with security audits. Manual audits cost $10K-$100K per project. Automated preliminary checks could reduce this by 80%.",
    source: "twitter",
    score: 83,
    tam: "$3B",
    sam: "$600M",
    som: "$30M",
    growth: "+55% YoY",
    competition: "Low",
    tags: ["Web3", "Security", "AI"],
    status: "discovered",
  },
]

export default function DiscoverPage() {
  const [searchQuery, setSearchQuery] = useState("")
  const [filterTag, setFilterTag] = useState<string | null>(null)
  const [scanning, setScanning] = useState(false)

  const allTags = Array.from(new Set(MOCK_OPPORTUNITIES.flatMap((o) => o.tags)))

  const filtered = MOCK_OPPORTUNITIES.filter((opp) => {
    const matchesSearch = !searchQuery || 
      opp.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
      opp.description.toLowerCase().includes(searchQuery.toLowerCase())
    const matchesTag = !filterTag || opp.tags.includes(filterTag)
    return matchesSearch && matchesTag
  })

  const handleScan = async () => {
    setScanning(true)
    // Simulate API call
    await new Promise((r) => setTimeout(r, 2000))
    setScanning(false)
  }

  const getScoreColor = (score: number) => {
    if (score >= 90) return "success"
    if (score >= 80) return "default"
    return "warning"
  }

  return (
    <div className="px-4 py-12 sm:px-6 lg:px-8">
      <div className="mx-auto max-w-6xl">
        {/* Header */}
        <div className="mb-10 text-center">
          <h1 className="text-3xl font-bold sm:text-4xl">Market Opportunity Scanner</h1>
          <p className="mt-3 text-lg text-muted-foreground">
            AI-powered discovery of high-value startup opportunities
          </p>
        </div>

        {/* Controls */}
        <div className="mb-8 flex flex-col gap-4 sm:flex-row">
          <Input
            placeholder="Search opportunities..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="flex-1"
          />
          <Button variant="glow" onClick={handleScan} disabled={scanning}>
            {scanning ? "🔍 Scanning..." : "🔄 Run New Scan"}
          </Button>
        </div>

        {/* Tag Filters */}
        <div className="mb-8 flex flex-wrap gap-2">
          <Badge
            variant={!filterTag ? "default" : "outline"}
            className="cursor-pointer"
            onClick={() => setFilterTag(null)}
          >
            All
          </Badge>
          {allTags.map((tag) => (
            <Badge
              key={tag}
              variant={filterTag === tag ? "default" : "outline"}
              className="cursor-pointer"
              onClick={() => setFilterTag(tag === filterTag ? null : tag)}
            >
              {tag}
            </Badge>
          ))}
        </div>

        {/* Results Count */}
        <p className="mb-6 text-sm text-muted-foreground">
          Showing {filtered.length} of {MOCK_OPPORTUNITIES.length} opportunities
        </p>

        {/* Opportunity Cards */}
        <div className="grid gap-6 md:grid-cols-2">
          {filtered.map((opp) => (
            <Card key={opp.id} className="group border-border/60 transition-all hover:border-primary/30 hover:shadow-lg">
              <CardHeader>
                <div className="flex items-start justify-between gap-4">
                  <div className="flex-1">
                    <CardTitle className="text-lg">{opp.title}</CardTitle>
                    <CardDescription className="mt-1">{opp.source}</CardDescription>
                  </div>
                  <Badge variant={getScoreColor(opp.score as number)} className="text-lg px-3 py-1">
                    {opp.score}
                  </Badge>
                </div>
              </CardHeader>
              <CardContent>
                <p className="mb-4 text-sm text-muted-foreground">{opp.description}</p>
                
                {/* Tags */}
                <div className="mb-4 flex flex-wrap gap-1.5">
                  {opp.tags.map((tag) => (
                    <Badge key={tag} variant="outline" className="text-xs">{tag}</Badge>
                  ))}
                </div>

                {/* Market Metrics */}
                <div className="grid grid-cols-2 gap-3 rounded-lg bg-muted/50 p-3 text-sm">
                  <div>
                    <span className="text-muted-foreground">TAM</span>
                    <span className="ml-2 font-semibold">{opp.tam}</span>
                  </div>
                  <div>
                    <span className="text-muted-foreground">SAM</span>
                    <span className="ml-2 font-semibold">{opp.sam}</span>
                  </div>
                  <div>
                    <span className="text-muted-foreground">Growth</span>
                    <span className="ml-2 font-semibold text-green-600">{opp.growth}</span>
                  </div>
                  <div>
                    <span className="text-muted-foreground">Competition</span>
                    <span className="ml-2 font-semibold">{opp.competition}</span>
                  </div>
                </div>

                {/* Actions */}
                <div className="mt-4 flex gap-2">
                  <Button size="sm" variant="default" className="flex-1">
                    Generate MVP
                  </Button>
                  <Button size="sm" variant="outline">
                    Details
                  </Button>
                </div>
              </CardContent>
            </Card>
          ))}
        </div>

        {filtered.length === 0 && (
          <div className="py-20 text-center">
            <p className="text-lg text-muted-foreground">No opportunities match your filters.</p>
            <Button variant="glow" className="mt-4" onClick={handleScan}>
              Run a Fresh Scan
            </Button>
          </div>
        )}
      </div>
    </div>
  )
}
