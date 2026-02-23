# 🎬 Movie Recommendation System

A production ready, content based Movie Recommendation Engine built using NLP techniques and deployed as a scalable web application.

This project demonstrates end-to-end Machine Learning system design from feature engineering and vector space modeling to model persistence and cloud deployment.

---

## 📌 Overview

This system leverages the **TMDB 5000 Movie Dataset (Kaggle)** to build a similarity-driven recommendation engine that suggests movies based on metadata analysis rather than user ratings.

Unlike collaborative filtering systems, this approach focuses on **content similarity**, making it robust for cold-start scenarios and metadata-driven discovery.

The solution is fully deployed using Flask + Gunicorn on Render, with dynamic poster integration via the TMDB API.

---

## 🏗 System Architecture
# 🎬 Movie Recommendation System

A production ready, content based Movie Recommendation Engine built using NLP techniques and deployed as a scalable web application.

This project demonstrates end-to-end Machine Learning system design from feature engineering and vector space modeling to model persistence and cloud deployment.

---

## 📌 Overview

This system leverages the **TMDB 5000 Movie Dataset (Kaggle)** to build a similarity driven recommendation engine that suggests movies based on metadata analysis rather than user ratings.

Unlike collaborative filtering systems, this approach focuses on **content similarity**, making it robust for cold start scenarios and metadata driven discovery.

The solution is fully deployed using Flask + Gunicorn on Render, with dynamic poster integration via the TMDB API.

---

## 🏗 System Architecture
Data Preprocessing (Offline)
↓
Feature Engineering + NLP
↓
Vectorization (CountVectorizer)
↓
Cosine Similarity Matrix
↓
Model Serialization (Pickle)
↓
Flask Inference API
↓
Frontend (Fetch API)
↓
TMDB Poster Retrieval


Key design principle:
- Heavy computation (vectorization + similarity matrix) is performed offline.
- Runtime inference is lightweight and optimized for low latency.

---

## 🚀 Core Features

- Content-based filtering using NLP
- Multi-field metadata aggregation
- Text normalization with stemming (NLTK)
- Bag-of-Words vectorization (max_features=5000)
- Cosine similarity-based ranking
- Model artifact persistence using Pickle
- REST-based inference API
- Cloud deployment using Gunicorn + Render
- Real-time TMDB API integration for movie posters

---

## 🧠 Machine Learning Pipeline

### Dataset

**TMDB 5000 Movie Dataset (Kaggle)**  
~4800 movies with structured metadata.

Key features utilized:

- `overview`
- `genres`
- `keywords`
- `cast`
- `crew`

---

### Feature Engineering

A unified `tags` feature was created by combining multiple metadata sources.

Processing steps included:

- Null value removal
- Standardization of categorical fields
- Removal of whitespace inconsistencies in entity names
- Lowercasing and token normalization
- Stemming using NLTK PorterStemmer
- Text consolidation into a single feature space

This ensures semantic consistency while reducing vocabulary dimensionality.

---

### Vectorization

```python
CountVectorizer(max_features=5000, stop_words='english')

Converts processed text into numerical feature vectors

Restricts vocabulary size for computational efficiency

Eliminates common stopwords
```

### Similarity Computation

Cosine similarity was computed across all movie vectors:

- Generates an NxN similarity matrix
- Enables fast top-K recommendation retrieval
- Avoids recomputation during inference

This matrix is serialized and loaded directly in production for real-time performance.

### 💾 Model Persistence Strategy

To ensure separation of concerns between training and serving:

- movie_dict.pkl → Serialized movie metadata
- similarity.pkl → Precomputed similarity matrix

## Advantages:
- Faster startup time
- No retraining required in production
- Reduced runtime computation cost
- Clear offline/online architecture split

### 🌐 Deployment Architecture

## Backend
- Flask REST API
- Gunicorn WSGI server

## Frontend
- Async Fetch API for dynamic recommendations
- JSON-based communication

## Cloud Hosting
- Render Web Service deployment
- Environment variable management for API keys

## External Integration
- TMDB API for poster retrieval
- Dynamic image rendering in UI

### ⚡ Runtime Flow

1. User selects a movie.
2. Backend identifies its index.
3. Similarity scores are retrieved from precomputed matrix.
4. Top 5 most similar movies are ranked.
5. Poster images are fetched via TMDB API.
6. JSON response is returned and rendered dynamically.

### 📊 Performance Considerations

- Precomputed similarity ensures constant-time lookup.
- Vector space limited to 5000 features for efficiency.
- Offline-heavy computation reduces production overhead.
- Lightweight Flask API ensures fast response cycles.

### 🛠 Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Flask
- Gunicorn
- Render
- TMDB API

### 📈 Engineering Highlights
- Clean separation between training and inference layers
- Production-ready deployment configuration
- RESTful API design
- Efficient similarity-based retrieval
- Real-world API integration
- Cloud-based hosting and environment configuration

### 🔮 Future Enhancements
- Hybrid recommendation system (content + collaborative)
- User interaction tracking
- Personalization layer
- Model optimization with TF-IDF
- Containerization using Docker
- CI/CD automation

### 👨‍💻 Author

Jignesh More (Machine Learning & Data Science Practitioner)