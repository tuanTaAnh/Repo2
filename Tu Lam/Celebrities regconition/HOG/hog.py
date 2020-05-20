from HOG.implement import FeatureExtraction


class HOG:
    @staticmethod
    def get_data_output(data_input):
        data_output = []
        for i in range(len(data_input)):
            vector = FeatureExtraction.hog(data_input[i])
            data_output.append(vector)
        return data_output




