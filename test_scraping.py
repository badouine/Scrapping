# test_scraping.py

from bs4 import BeautifulSoup
import pandas as pd

def exercice1(html_content):
    """Test pour l'extraction des titres et liens des actualités"""
    html_test = """
    <!DOCTYPE html>
    <html>
    <head><title>Example News Site</title></head>
    <body>
    <div class="news">
        <h2><a href="https://example-news-site.com/article1">Titre de l'article 1</a></h2>
        <p>Contenu de l'article 1...</p>
    </div>
    <div class="news">
        <h2><a href="https://example-news-site.com/article2">Titre de l'article 2</a></h2>
        <p>Contenu de l'article 2...</p>
    </div>
    </body>
    </html>
    """
    
    soup = BeautifulSoup(html_test, 'html.parser')
    articles = []
    
    for article in soup.find_all('div', class_='news'):
        link = article.find('a')
        articles.append({
            'titre': link.text,
            'url': link['href']
        })
    
    return pd.DataFrame(articles)

def exercice2(html_content):
    """Test pour l'extraction des produits"""
    html_test = """
    <!DOCTYPE html>
    <html>
    <head><title>Example Products</title></head>
    <body>
    <div class="product">
        <h3>Nom du produit 1</h3>
        <p>Prix: 10.99 EUR</p>
    </div>
    <div class="product">
        <h3>Nom du produit 2</h3>
        <p>Prix: 25.50 EUR</p>
    </div>
    </body>
    </html>
    """
    
    soup = BeautifulSoup(html_test, 'html.parser')
    products = []
    
    for product in soup.find_all('div', class_='product'):
        name = product.find('h3').text
        price = product.find('p').text.split(':')[1].strip()
        products.append({
            'nom': name,
            'prix': price
        })
    
    return pd.DataFrame(products)

# Ajoutez les autres exercices ici...

def main():
    """Fonction de test individuel"""
    print("=== Test individuel des exercices ===")
    print("\nTest Exercice 1:")
    print(exercice1(None))
    print("\nTest Exercice 2:")
    print(exercice2(None))

if __name__ == "__main__":
    main()