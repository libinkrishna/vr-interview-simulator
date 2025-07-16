from src import vr_environment, ai_interviewer, sentiment_analysis

def main():
    print('VR Interview Simulator starting...')

    vr_environment.load_environment('Tech Interview Room')
    question = ai_interviewer.generate_question()
    user_response = input('Your answer: ')

    sentiment = sentiment_analysis.analyze_sentiment(user_response)
    print(f'Sentiment analysis result: {sentiment}')

if __name__ == '__main__':
    main()

