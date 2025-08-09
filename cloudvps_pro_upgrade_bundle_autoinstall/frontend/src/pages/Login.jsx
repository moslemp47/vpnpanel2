import React from 'react'
import { Link } from 'react-router-dom'

export default function Login() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
      <div className="w-full max-w-md p-6 bg-white rounded-2xl shadow border">
        <h1 className="text-2xl font-bold text-gray-800 mb-4">Login</h1>
        <form className="space-y-3">
          <input className="w-full border rounded-xl p-2" placeholder="Email" />
          <input className="w-full border rounded-xl p-2" placeholder="Password" type="password" />
          <div className="text-sm text-gray-500">Captcha here</div>
          <button className="w-full bg-blue-600 text-white rounded-xl py-2">Sign in</button>
        </form>
        <div className="text-sm mt-3">
          <a href="#" className="text-blue-600">Forgot password?</a>
        </div>
        <div className="text-sm mt-1">
          No account? <a href="#" className="text-blue-600">Sign up</a>
        </div>
        <div className="mt-6">
          <Link to="/" className="text-gray-500">← Back to site</Link>
        </div>
      </div>
    </div>
  )
}
