import { render, screen, fireEvent } from '@testing-library/react'
import '@testing-library/jest-dom'
import Home from '../app/page'

describe('Home', () => {
  it('renders the main heading', () => {
    render(<Home />)
    expect(screen.getByText('FastAPI React PostgreSQL Boilerplate')).toBeInTheDocument()
  })

  it('renders login form', () => {
    render(<Home />)
    expect(screen.getByText('Login')).toBeInTheDocument()
    expect(screen.getByPlaceholderText('Enter your email')).toBeInTheDocument()
    expect(screen.getByPlaceholderText('Enter your password')).toBeInTheDocument()
  })

  it('renders features section', () => {
    render(<Home />)
    expect(screen.getByText('Features')).toBeInTheDocument()
    expect(screen.getByText('FastAPI Backend')).toBeInTheDocument()
    expect(screen.getByText('PostgreSQL Database')).toBeInTheDocument()
  })

  it('handles form submission', () => {
    const consoleSpy = jest.spyOn(console, 'log').mockImplementation()
    render(<Home />)
    
    const emailInput = screen.getByPlaceholderText('Enter your email')
    const passwordInput = screen.getByPlaceholderText('Enter your password')
    const submitButton = screen.getByText('Sign In')

    fireEvent.change(emailInput, { target: { value: 'test@example.com' } })
    fireEvent.change(passwordInput, { target: { value: 'password123' } })
    fireEvent.click(submitButton)

    expect(consoleSpy).toHaveBeenCalledWith('Login attempt:', {
      email: 'test@example.com',
      password: 'password123'
    })

    consoleSpy.mockRestore()
  })
}) 