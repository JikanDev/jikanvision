from distutils.core import setup

setup(
  name = 'jikanvision',         # How you named your package folder (MyLib)
  packages = ['jikanvision'],   # Chose the same as "name"
  version = '0.4',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'My library for AI Computer Vision based on Mediapipe and OpenCV',   # Give a short description about your library
  author = 'JikanDev',                   # Type in your name
  author_email = 'jikandev@gmail.com',      # Type in your E-Mail
  url = 'https://jikandev.xyz/',   # Provide either the link to your github or to your website
  project_urls={
    "Bug Tracker": "https://github.com/JikanDev/jikanvision/issues",
  },
  keywords = ['Computer Vision', 'Face Detection', 'Hands Tracking', 'Bodies Tracking'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'opencv-python==4.5.3.56',
          'mediapipe==0.8.7.3',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license.
    'Programming Language :: Python :: 3.6',    #Specify which python versions that you want to support.
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)