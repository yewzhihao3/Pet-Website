# Eric's Exotic Pet Farm - Django Website

[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-blue?style=for-the-badge&logo=github)](https://github.com/yewzhihao3/Pet-Website)
[![Live Website](https://img.shields.io/badge/Live-Website-green?style=for-the-badge&logo=render)](https://pet-website-bpxk.onrender.com)

A Django-based web application for showcasing and selling exotic pets in Malaysia. This website serves as a digital catalog for Eric's Exotic Pet Farm, featuring a collection of unique and rare animals from around the world.

## 🐾 About the Project

Eric's Exotic Pet Farm is your trusted destination for rare and fascinating exotic pets. Whether you're looking for a unique companion or expanding your collection, we provide healthy, well-cared-for animals that you won't find in regular pet shops.

### Features

- **Pet Catalog**: Browse through a diverse collection of exotic pets including reptiles, amphibians, rare mammals, and birds
- **Detailed Pet Information**: Each pet listing includes comprehensive details, images, and care requirements
- **Interactive Gallery**: Beautiful image galleries showcasing each exotic pet
- **Contact Integration**: WhatsApp integration for easy communication
- **Location Services**: Interactive map and navigation to the farm location
- **Responsive Design**: Mobile-friendly interface for all devices

### Pet Categories

- **Reptiles**: Iguanas, tortoises, and other exotic reptiles
- **Mammals**: Sugar gliders, marmosets, meerkats, and other unique mammals
- **Birds**: Various exotic bird species
- **Amphibians**: Specialized amphibian species

## 🚀 Technology Stack

- **Backend**: Django (Python web framework)
- **Database**: SQLite (development) / PostgreSQL (production)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with responsive design
- **Icons**: Font Awesome
- **Maps**: Google Maps integration
- **Hosting**: [Render](https://render.com) - Cloud hosting platform
- **Monitoring**: [UptimeRobot](https://uptimerobot.com) - Website uptime monitoring

## 📁 Project Structure

```
backend/
├── myapp/                    # Main Django application
│   ├── models.py            # Pet and Category models
│   ├── views.py             # View functions
│   ├── urls.py              # URL routing
│   ├── admin.py             # Django admin configuration
│   ├── templates/           # HTML templates
│   │   └── pets/
│   │       ├── index.html   # Home page
│   │       ├── about.html   # About page
│   │       ├── ourpets.html # Pet catalog
│   │       └── components/  # Reusable components
│   └── static/              # Static files (CSS, JS, images)
├── petwebsite/              # Django project settings
│   ├── settings.py          # Project configuration
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py              # WSGI configuration
├── media/                   # User-uploaded files (pet images)
├── staticfiles/             # Collected static files
├── requirements.txt         # Python dependencies
└── manage.py               # Django management script
```

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Local Development

1. **Clone the repository**

   ```bash
   git clone https://github.com/yewzhihao3/Pet-Website.git
   cd Pet-Website/backend
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional)**

   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**

   ```bash
   python manage.py runserver
   ```

7. **Access the website**
   - **Live Site**: [https://pet-website-bpxk.onrender.com](https://pet-website-bpxk.onrender.com)
   - **Local Development**: http://127.0.0.1:8000/
   - **Admin Panel**: http://127.0.0.1:8000/admin/ (local) or [https://pet-website-bpxk.onrender.com/admin/](https://pet-website-bpxk.onrender.com/admin/) (live)

## 📱 Pages & Features

### Home Page (`/`)

- Hero section with slideshow
- Featured pets showcase
- Quick navigation to other sections

### About Page (`/about/`)

- Company mission and values
- Why choose Eric's Exotic Pet Farm
- Location and contact information
- Interactive map integration

### Pet Catalog (`/ourpets/`)

- Grid layout of all available pets
- Filter by category
- Detailed pet information modals
- High-quality pet images

## 🗄️ Database Models

### Pet Model

- Name, description, price
- Category classification
- Availability status
- High-quality images
- Care requirements

### Category Model

- Pet category classification
- Category descriptions

## 🎨 Design Features

- **Responsive Design**: Optimized for desktop, tablet, and mobile
- **Modern UI**: Clean, professional interface
- **Smooth Animations**: CSS animations and transitions
- **Interactive Elements**: Hover effects and modal dialogs
- **Accessibility**: Screen reader friendly

## 📍 Location

**Eric's Exotic Pet Farm**
4, Jalan Bunga Raya, Assam Kumbang, 34000 Taiping, Perak, Malaysia

## 🌐 Live Website

**Visit the live website**: [https://pet-website-bpxk.onrender.com](https://pet-website-bpxk.onrender.com)

The website is hosted on Render with UptimeRobot monitoring to ensure consistent availability.

## 🤝 Contributing

This is a private project for Eric's Exotic Pet Farm. For any inquiries or suggestions, please contact the farm directly.

## 📄 License

This project is proprietary to Eric's Exotic Pet Farm.

## 📞 Contact

- **Live Website**: [https://pet-website-bpxk.onrender.com](https://pet-website-bpxk.onrender.com)
- **WhatsApp**: Available through the website's floating WhatsApp button
- **Location**: 4, Jalan Bunga Raya, Assam Kumbang, 34000 Taiping, Perak, Malaysia
- **GitHub Repository**: [Eric's Exotic Pet Farm](https://github.com/yewzhihao3/Pet-Website)

---

_At Eric's Exotic Pet Farm, we don't just sell pets – we help you begin a rewarding journey with a truly unique companion._
