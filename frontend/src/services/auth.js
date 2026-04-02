import { authService } from './api';

export const login = async (email, password) => {
  try {
    const response = await authService.login({ email, password });
    localStorage.setItem('token', response.access_token);
    return response;
  } catch (error) {
    throw error.response?.data?.detail || 'Login failed';
  }
};

export const signup = async (email, password) => {
  try {
    const response = await authService.signup({ email, password });
    return response;
  } catch (error) {
    throw error.response?.data?.detail || 'Signup failed';
  }
};

export const logout = () => {
  localStorage.removeItem('token');
};

export const getToken = () => {
  return localStorage.getItem('token');
};

export const isAuthenticated = () => {
  return !!getToken();
};
