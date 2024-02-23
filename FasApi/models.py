class song_predictions():
    def predict(self, song):
        model = "model"
        prediction = model.predict(song)
        return {prediction}

