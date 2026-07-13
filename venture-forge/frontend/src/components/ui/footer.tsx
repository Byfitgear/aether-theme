import Link from "next/link"

export function Footer() {
  return (
    <footer className="border-t border-border/40 bg-muted/30">
      <div className="mx-auto max-w-7xl px-4 py-12 sm:px-6 lg:px-8">
        <div className="grid grid-cols-2 gap-8 md:grid-cols-4">
          <div>
            <h3 className="font-semibold text-foreground">Product</h3>
            <ul className="mt-4 space-y-2 text-sm text-muted-foreground">
              <li><Link href="/discover" className="hover:text-foreground">Discover</Link></li>
              <li><Link href="/pricing" className="hover:text-foreground">Pricing</Link></li>
              <li><Link href="#" className="hover:text-foreground">Changelog</Link></li>
            </ul>
          </div>
          <div>
            <h3 className="font-semibold text-foreground">Resources</h3>
            <ul className="mt-4 space-y-2 text-sm text-muted-foreground">
              <li><Link href="#" className="hover:text-foreground">Documentation</Link></li>
              <li><Link href="#" className="hover:text-foreground">API Reference</Link></li>
              <li><Link href="#" className="hover:text-foreground">Blog</Link></li>
            </ul>
          </div>
          <div>
            <h3 className="font-semibold text-foreground">Company</h3>
            <ul className="mt-4 space-y-2 text-sm text-muted-foreground">
              <li><Link href="#" className="hover:text-foreground">About</Link></li>
              <li><Link href="#" className="hover:text-foreground">Careers</Link></li>
              <li><Link href="#" className="hover:text-foreground">Contact</Link></li>
            </ul>
          </div>
          <div>
            <h3 className="font-semibold text-foreground">Legal</h3>
            <ul className="mt-4 space-y-2 text-sm text-muted-foreground">
              <li><Link href="#" className="hover:text-foreground">Privacy</Link></li>
              <li><Link href="#" className="hover:text-foreground">Terms</Link></li>
            </ul>
          </div>
        </div>
        <div className="mt-8 border-t border-border/40 pt-8 text-center text-sm text-muted-foreground">
          © 2025 VentureForge. All rights reserved.
        </div>
      </div>
    </footer>
  )
}
