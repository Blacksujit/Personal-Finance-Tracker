# 🚀 Netlify Deployment Guide - Personal Finance Tracker

## 📋 Prerequisites
- Netlify account (free)
- Git repository (GitHub/GitLab/Bitbucket)
- Production backend URL (Railway/Render/Heroku)

## 🏗️ Deployment Steps

### 1. **Push Code to Git Repository**
```bash
git add .
git commit -m "Ready for Netlify deployment"
git push origin main
```

### 2. **Deploy to Netlify**

#### Option A: Drag & Drop (Easiest)
1. Go to [netlify.com](https://netlify.com)
2. Sign in/up
3. Drag the `frontend/dist` folder to the deploy area
4. Your site will be live instantly!

#### Option B: Git Integration (Recommended)
1. Go to [netlify.com](https://netlify.com)
2. Click "Add new site" → "Import an existing project"
3. Connect your Git provider
4. Select your repository
5. Configure build settings:
   - **Build command**: `npm run build`
   - **Publish directory**: `dist`
   - **Base directory**: `frontend`
6. Click "Deploy site"

### 3. **Configure Environment Variables**
In Netlify dashboard → Site settings → Environment variables:
```
VITE_API_URL=https://your-backend-url.com/api
```

### 4. **Update Backend CORS**
Add your Netlify URL to backend CORS allowed origins:
```python
# In backend/main.py
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://your-netlify-site.netlify.app"  # Add this
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## 🔧 Configuration Files Created

### `frontend/netlify.toml`
- Build settings
- Redirects for API calls
- SPA routing support

### `frontend/.env.production`
- Production environment variables
- API URL configuration

## 🌐 After Deployment

### 1. **Update API URL**
Replace `https://your-backend-url.com/api` with your actual backend URL in:
- Netlify environment variables
- `frontend/.env.production`

### 2. **Test Your Live Site**
- Visit your Netlify URL
- Test login/registration
- Verify all features work

### 3. **Custom Domain (Optional)**
- Go to Site settings → Domain management
- Add custom domain
- Update DNS records

## 📱 Quick Deploy Commands

```bash
# Build and test locally
cd frontend
npm run build

# Deploy to Netlify (CLI required)
npm install -g netlify-cli
netlify deploy --prod --dir=dist
```

## 🚨 Important Notes

1. **Backend URL**: Must update `VITE_API_URL` with your production backend
2. **CORS**: Backend must allow your Netlify domain
3. **Environment Variables**: Set in Netlify dashboard, not code
4. **HTTPS**: Netlify provides free SSL certificates

## 🎯 Production Checklist

- [ ] Backend deployed and accessible
- [ ] CORS configured for Netlify domain
- [ ] Environment variables set in Netlify
- [ ] Test all functionality on live site
- [ ] Custom domain configured (if needed)

## 🔗 Useful Links

- [Netlify Documentation](https://docs.netlify.com/)
- [Netlify Deploy Guide](https://docs.netlify.com/sites/deployment/)
- [Environment Variables](https://docs.netlify.com/configure-builds/environment-variables/)

---

**Your Personal Finance Tracker will be live on Netlify! 🎉**
