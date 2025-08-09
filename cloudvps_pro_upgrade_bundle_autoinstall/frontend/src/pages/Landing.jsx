import React from 'react'
import { Link } from 'react-router-dom'

export default function Landing() {
  return (
    <div className="min-h-screen flex flex-col">
      <header className="bg-white/80 backdrop-blur sticky top-0 z-40 border-b">
        <div className="max-w-6xl mx-auto flex items-center justify-between p-4">
          <div className="text-2xl font-bold text-blue-700">CloudVPS Pro</div>
          <nav className="space-x-6 text-gray-700">
            <a href="#">Home</a>
            <a href="#plans">VPS Plans</a>
            <a href="#features">Features</a>
            <a href="#about">About</a>
            <a href="#contact">Contact</a>
            <Link to="/login" className="font-semibold">Login</Link>
          </nav>
        </div>
      </header>

      <main className="flex-1">
        <section className="bg-gradient-to-b from-blue-700 to-blue-500 text-white">
          <div className="max-w-6xl mx-auto px-4 py-24 text-center">
            <h1 className="text-4xl md:text-6xl font-extrabold">Premium VPS Hosting Solutions</h1>
            <p className="mt-4 text-lg text-blue-100">
              High Performance Virtual Servers with 99.9% uptime, NVMe SSDs and DDoS protection.
            </p>
            <Link to="/login" className="inline-block mt-6 px-6 py-3 bg-white text-blue-700 rounded-xl shadow hover:opacity-90">
              Get Started
            </Link>
          </div>
        </section>

        <section id="plans" className="py-16 bg-gray-50">
          <div className="max-w-6xl mx-auto px-4">
            <h2 className="text-3xl font-bold text-gray-800 text-center mb-8">VPS Plans</h2>
            <div className="grid md:grid-cols-3 gap-6">
              {([
                {name:'Basic VPS', price:'$6.99/mo', cpu:'1 vCPU', ram:'1GB', disk:'20GB NVMe', bw:'1TB'},
                {name:'Pro VPS', price:'$12.99/mo', cpu:'2 vCPU', ram:'2GB', disk:'40GB NVMe', bw:'2TB'},
                {name:'Enterprise VPS', price:'$29.99/mo', cpu:'4 vCPU', ram:'8GB', disk:'120GB NVMe', bw:'6TB'},
              ]).map((p, i) => (
                <div key={i} className="bg-white rounded-2xl shadow p-6 border">
                  <div className="text-xl font-semibold text-gray-800">{p.name}</div>
                  <div className="text-3xl font-bold text-blue-700 my-3">{p.price}</div>
                  <ul className="text-gray-600 space-y-1">
                    <li>{p.cpu}</li><li>{p.ram}</li><li>{p.disk}</li><li>{p.bw} bandwidth</li>
                  </ul>
                  <Link to="/login" className="mt-6 inline-block w-full text-center bg-blue-600 text-white rounded-xl py-2">Choose</Link>
                </div>
              ))}
            </div>
          </div>
        </section>

        <section id="features" className="py-16 bg-white">
          <div className="max-w-6xl mx-auto px-4 grid md:grid-cols-3 gap-6">
            {[
              {title:'99.9% Uptime', desc:'Reliable infrastructure for mission-critical workloads.'},
              {title:'NVMe SSD', desc:'Blazing fast I/O for your apps and databases.'},
              {title:'DDoS Protection', desc:'Edge filtering and WAF to keep you safe.'},
            ].map((f, i) => (
              <div key={i} className="p-6 rounded-2xl border shadow-sm">
                <div className="text-2xl font-bold text-blue-700">{f.title}</div>
                <div className="text-gray-600 mt-2">{f.desc}</div>
              </div>
            ))}
          </div>
        </section>

        <section id="about" className="py-16 bg-gray-50">
          <div className="max-w-6xl mx-auto px-4">
            <h2 className="text-3xl font-bold text-gray-800 mb-3">About</h2>
            <p className="text-gray-600">
              CloudVPS Pro is a premium virtual server provider with global locations and enterprise-grade hardware.
            </p>
          </div>
        </section>

        <section id="contact" className="py-16 bg-white">
          <div className="max-w-6xl mx-auto px-4">
            <h2 className="text-3xl font-bold text-gray-800 mb-3">Contact</h2>
            <p className="text-gray-600">Email: support@example.com</p>
          </div>
        </section>
      </main>

      <footer className="bg-gray-900 text-gray-300">
        <div className="max-w-6xl mx-auto p-6 grid md:grid-cols-3 gap-6">
          <div>
            <div className="text-white font-bold text-xl">CloudVPS Pro</div>
            <p className="text-sm mt-2">High Performance Virtual Servers</p>
          </div>
          <div>
            <div className="font-semibold">Links</div>
            <ul className="mt-2 space-y-1 text-sm">
              <li><a href="#">Terms</a></li>
              <li><a href="#">Privacy</a></li>
              <li><a href="#">Status</a></li>
            </ul>
          </div>
          <div>
            <div className="font-semibold">Social</div>
            <div className="flex space-x-3 mt-2">
              <a href="#">Twitter</a>
              <a href="#">GitHub</a>
              <a href="#">Telegram</a>
            </div>
          </div>
        </div>
        <div className="text-center text-xs py-3 border-t border-gray-800">© {new Date().getFullYear()} CloudVPS Pro</div>
      </footer>
    </div>
  )
}
