# Deploying Pet Website to Render

This guide will help you deploy your Django pet website to Render using SQLite.

## Prerequisites

1. A GitHub account
2. A Render account (sign up at https://render.com)
3. Your project pushed to GitHub

## Step 1: Prepare Your Repository

1. **Push your code to GitHub** (if not already done):
   ```bash
   git add .
   git commit -m "Prepare for Render deployment"
   git push origin main
   ```

## Step 2: Deploy to Render

1. **Go to Render Dashboard**:

   - Visit https://dashboard.render.com
   - Sign in with your GitHub account

2. **Create a New Web Service**:

   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select your pet website repository

3. **Configure the Service**:

   - **Name**: `pet-website` (or any name you prefer)
   - **Environment**: `Python 3`
   - **Build Command**:
     ```bash
     pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
     ```
   - **Start Command**:
     ```bash
     gunicorn petwebsite.wsgi:application
     ```

4. **Environment Variables** (Optional but recommended):

   - `DEBUG`: `False`
   - `SECRET_KEY`: Generate a new secret key (you can use Django's built-in key generator)
   - `ALLOWED_HOSTS`: `your-app-name.onrender.com` (replace with your actual app name)

5. **Deploy**:
   - Click "Create Web Service"
   - Render will automatically build and deploy your application

## Step 3: Post-Deployment Setup

1. **Create a Superuser** (for admin access):

   - Go to your deployed app URL + `/admin/`
   - You'll need to create a superuser account
   - You can do this by running Django shell commands or using Render's shell feature

2. **Add Your Pet Data**:
   - Access the Django admin panel
   - Add your pet categories and pet information
   - Upload pet images

## Important Notes

### SQLite Limitations on Render

- **Data Persistence**: SQLite files on Render are ephemeral and will be lost when the service restarts
- **For Production**: Consider upgrading to a PostgreSQL database for data persistence
- **For Development/Testing**: SQLite is fine for small projects

### Static Files

- Static files are automatically collected during build
- WhiteNoise middleware serves static files efficiently
- Media files (pet images) are stored in the `/media/` directory

### Environment Variables

The app uses these environment variables:

- `DEBUG`: Controls debug mode (set to `False` in production)
- `SECRET_KEY`: Django secret key for security
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts

## Troubleshooting

### Common Issues:

1. **Build Failures**: Check that all dependencies are in `requirements.txt`
2. **Static Files Not Loading**: Ensure `collectstatic` runs during build
3. **Database Issues**: Make sure migrations are applied
4. **Media Files**: Remember that uploaded files will be lost on restart with SQLite

### Getting Help:

- Check Render's build logs for error messages
- Ensure your `render.yaml` file is properly configured
- Verify all environment variables are set correctly

## Next Steps (Optional)

For a production-ready deployment, consider:

1. **Upgrading to PostgreSQL**: For persistent data storage
2. **Adding a CDN**: For better static file delivery
3. **Setting up monitoring**: For application health checks
4. **Configuring custom domain**: For a professional URL

Your pet website should now be live on Render! 🐾
