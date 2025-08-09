import React from 'react'
import { Routes, Route, Link } from 'react-router-dom'

function Dashboard(){ return <div>Dashboard: users, subs, MRR charts</div> }
function Users(){ return <div>Users list with search/filter</div> }
function Plans(){ return <div>Plans with limits (bandwidth, connections, device limit)</div> }
function Servers(){ return <div>Manage Marzban/Sanaei servers</div> }
function Logs(){ return <div>Activity logs (login, purchases, API calls)</div> }
function Finance(){ return <div>Reports (daily/weekly/monthly)</div> }
function Settings(){ return <div>SMTP, Payment gateways, Maintenance mode</div> }
function Tickets(){ return <div>Support tickets</div> }

export default function Admin(){
  return (
    <div className="min-h-screen grid grid-cols-5">
      <aside className="col-span-1 border-r p-4 space-y-2">
        <Link to="" className="block">Dashboard</Link>
        <Link to="users" className="block">Users</Link>
        <Link to="plans" className="block">Plans</Link>
        <Link to="servers" className="block">Servers</Link>
        <Link to="logs" className="block">Logs</Link>
        <Link to="finance" className="block">Finance</Link>
        <Link to="settings" className="block">Settings</Link>
        <Link to="tickets" className="block">Tickets</Link>
      </aside>
      <main className="col-span-4 p-6">
        <Routes>
          <Route index element={<Dashboard/>} />
          <Route path="users" element={<Users/>} />
          <Route path="plans" element={<Plans/>} />
          <Route path="servers" element={<Servers/>} />
          <Route path="logs" element={<Logs/>} />
          <Route path="finance" element={<Finance/>} />
          <Route path="settings" element={<Settings/>} />
          <Route path="tickets" element={<Tickets/>} />
        </Routes>
      </main>
    </div>
  )
}
