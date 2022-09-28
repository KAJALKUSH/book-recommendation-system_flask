from flask import Flask, request, render_template
import pickle

books = pickle.load(open('books.pkl', 'rb'))
similarity = pickle.load(open('similarity_scores.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',
                           book_name=list(books['Title'].values),
                           author=list(books['Author'].values),
                           publisher=list(books['Publisher'].values),
                           genre=list(books['Genre'].values),
                           subgenre=list(books['SubGenre'].values)
                           )


@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')


@app.route('/recommend_books', methods=['post'])
def recommend():
    try:
        user_input = request.form.get('user_input')
        index = books[books['Title'] == user_input].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        data = []
        for i in distances[1:5]:
            #data = books.iloc[i[0]][['Title', 'Genre']]

            data.append(books.iloc[i[0]].Title)
        print(data)
        return render_template('recommend.html', data=data)
    except Exception as e:
        print('ERROR in recommend_books -> ', e)


if __name__ == '__main__':
    app.run(debug=True)
