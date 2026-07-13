"use client"

import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"

const DASHBOARD_STATS = [
  { label: "Active Projects", value: "3", change: "+1 this week", positive: true },
  { label: "Opportunities Found", value: "47", change: "Last 30 days", positive: true },
  { label: "Top Score", value: "92", change: "AI Support for E-commerce", positive: true },
  { label: "Deployed Products", value: "1", change: "In production", positive: true },
]

const RECENT_PROJECTS = [
  { name: "ShopBot AI", status: "deployed", url: "shopbot-ai.vercel.app", created: "2 days ago" },
  { name: "ComplyCheck", status: "building", url: null, created: "5 days ago" },
  { name: "SentimentFlow", status: "generated", url: null, created: "1 week ago" },
]

const METRICS_DATA = [
  { name: "Retention (Day 30)", value: 38, benchmark: 40, unit: "%" },
  { name: "Conversion Rate", value: 4.2, benchmark: 5, unit: "%" },
  { name: "CAC", value: 12, benchmark: 15, unit: "$" },
  { name: "LTV", value: 620, benchmark: 500, unit: "$" },
  { name: "MAU", value: 1240, benchmark: 1000, unit: "" },
  { name: "NPS", value: 52, benchmark: 50, unit: "" },
]

export default function DashboardPage() {
  const getMetricStatus = (value: number, benchmark: number) => {
    if (value >= benchmark) return "success" as const
    return "warning" as const
  }

  const getStatusBadge = (status: string) => {
    const map: Record<string, { variant: "success" | "default" | "outline"; label: string }> = {
      deployed: { variant: "success", label: "Live" },
      building: { variant: "default", label: "Building" },
      generated: { variant: "outline", label: "Generated" },
    }
    const s = map[status] || map.generated
    return <Badge variant={s.variant}>{s.label}</Badge>
  }

  return (
    <div className="px-4 py-12 sm:px-6 lg:px-8">
      <div className="mx-auto max-w-6xl">
        <div className="mb-10 flex items-center justify-between">
          <div>
            <h1 className="text-3xl font-bold sm:text-4xl">Dashboard</h1>
            <p className="mt-2 text-muted-foreground">Track your startup metrics and projects</p>
          </div>
          <Button variant="glow" href="/discover">+ New Opportunity</Button>
        </div>

        <div className="mb-10 grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
          {DASHBOARD_STATS.map((stat) => (
            <Card key={stat.label}>
              <CardContent className="pt-6">
                <p className="text-sm text-muted-foreground">{stat.label}</p>
                <p className="mt-2 text-3xl font-bold">{stat.value}</p>
                <p className="mt-1 text-xs text-green-600">{stat.change}</p>
              </CardContent>
            </Card>
          ))}
        </div>

        <Card className="mb-10">
          <CardHeader>
            <CardTitle>Growth Metrics</CardTitle>
            <CardDescription>Latest values vs. industry benchmarks</CardDescription>
          </CardHeader>
          <CardContent>
            <div className="overflow-x-auto">
              <table className="w-full text-sm">
                <thead>
                  <tr className="border-b border-border text-left text-muted-foreground">
                    <th className="pb-3 pr-4 font-medium">Metric</th>
                    <th className="pb-3 pr-4 font-medium">Value</th>
                    <th className="pb-3 pr-4 font-medium">Benchmark</th>
                    <th className="pb-3 font-medium">Status</th>
                  </tr>
                </thead>
                <tbody>
                  {METRICS_DATA.map((m) => (
                    <tr key={m.name} className="border-b border-border/40 last:border-0">
                      <td className="py-3 pr-4 font-medium">{m.name}</td>
                      <td className="py-3 pr-4">
                        <span className="font-semibold">{m.value}{m.unit}</span>
                      </td>
                      <td className="py-3 pr-4 text-muted-foreground">{m.benchmark}{m.unit}</td>
                      <td className="py-3">
                        <Badge variant={getMetricStatus(m.value, m.benchmark)} className="text-xs">
                          {m.value >= m.benchmark ? "✓ On Track" : "⚠ Needs Work"}
                        </Badge>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </CardContent>
        </Card>

        <div className="grid gap-6 lg:grid-cols-3">
          <Card className="lg:col-span-2">
            <CardHeader>
              <CardTitle>Recent Projects</CardTitle>
              <CardDescription>Your generated MVP projects</CardDescription>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                {RECENT_PROJECTS.map((project) => (
                  <div key={project.name} className="flex items-center justify-between rounded-lg border border-border/40 p-4">
                    <div>
                      <p className="font-medium">{project.name}</p>
                      <p className="text-sm text-muted-foreground">
                        Created {project.created}
                        {project.url && ` → ${project.url}`}
                      </p>
                    </div>
                    {getStatusBadge(project.status)}
                  </div>
                ))}
              </div>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>Quick Actions</CardTitle>
            </CardHeader>
            <CardContent className="space-y-3">
              <Button variant="glow" className="w-full" href="/discover">🔍 Scan Market</Button>
              <Button variant="outline" className="w-full" href="/discover">📊 View Opportunities</Button>
              <Button variant="outline" className="w-full" href="#">⚙️ Settings</Button>
            </CardContent>
          </Card>
        </div>
      </div>
    </div>
  )
}
