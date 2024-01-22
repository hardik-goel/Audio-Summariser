from setuptools import setup, find_packages

setup(
    name='AudioSummariser',
    version='0.1.1',
    long_description = open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        "setuptools-rust",
        "openai-whisper",
        "ffmpeg",
        "tiktoken",
        "tokenizers",
        "torch",
        "transformers",
        "google-cloud-aiplatform"
        "google-generativeai",
        "nltk",
        "wordcloud",
        "matplotlib",
    ],
    entry_points={
        'console_scripts': [
            'your_script_name = entry_handler:main'
        ],
    },

    author='Hardik Goel',
    author_email='hardik.goel214@gmail.com',
    description='Summarises the text generated from the audio files for quicker resolution. The audio files are '
                'typically the customer support recordings for now but the usecase can be extended to more '
                'dimensions. Sentiment is analysed and depicted visually.',
    url='https://github.com/hardik-goel/Audio-Summariser',
)
