import os.path
import os
import shutil
import urllib.request
import pymongo
from sys import stdout
from time import sleep


client = pymongo.MongoClient("localhost", 27017)
db = client.discogs_masters

# urllist = ["https://i.scdn.co/image/2484cbce6034b5a4f5dcdefe9396f3e51c8f905c","https://i.scdn.co/image/8fcb00e9598d7bc9484c163110892e759505cd44","https://i.scdn.co/image/2e8f33da249a6a24fa3569427575217365c156c0","https://i.scdn.co/image/7743bfccf903207bcc7df7b690d5535181c26f7d","https://i.scdn.co/image/c91bcb1b2217354baccc50aada82c76a4568cb83","https://i.scdn.co/image/d285d844d1411f910c1693f05867e7a1c32b22f1","https://i.scdn.co/image/69bb2f1b780964ad3789bdf6cd6de56b41e1c905","https://i.scdn.co/image/756c580ba4b55320c5004957ac2dc8d6970dfb40","https://i.scdn.co/image/9e61413a543b139d663c03838c65bf065fe03e9d","https://i.scdn.co/image/cede55447842b45b233158e6f7d2625c04d2d782","https://i.scdn.co/image/a1d0f7cfc68ee2159b2857de50039ce942678a52","https://i.scdn.co/image/4ca6185e9189a47c164044403b17a1803cba25ff","https://i.scdn.co/image/77eb7c17cafe5503a8484101e5ea2e8f937e1826","https://i.scdn.co/image/6e7cf2fe33c3fcacfbfa11db0088389d05794c76","https://i.scdn.co/image/9474837f9703fede3da3045059d8b33f062b1ce7","https://i.scdn.co/image/2098a9286b1057e1ac79f0e3693c9f316c203ade","https://i.scdn.co/image/d4e2d5cd8330112f67b61f37d747ba8a2bf9412c","https://i.scdn.co/image/fd1a62c7d654c5f048a47f12211ff62f90ed5a8f","https://i.scdn.co/image/920b5d37b9c4e1f2ea2ef8305347e10541caa5a7","https://i.scdn.co/image/ff791466a59f5505fa94e2404b7a679a64ee6496","https://i.scdn.co/image/db9c610bf304c8d22c11bca66db9479d566c3679","https://i.scdn.co/image/7f3afc1788cc8f842dc73f247c2a1078813f367b","https://i.scdn.co/image/abccbaf0dc9ab5e5437e68e40da7abbaba29c93c","https://i.scdn.co/image/57555ff872b3fafde75f8c0d8aa714b538778a6c","https://i.scdn.co/image/77eb7c17cafe5503c3efe7454f721ceece7b2fbb","https://i.scdn.co/image/6301845ad60db4a8cfc9740d7f79a19221309c40","https://i.scdn.co/image/bd8c592720a4f259dc95da52d26778b316103929","https://i.scdn.co/image/33d477d4b01beaef131424bf33182f24bdcef402","https://i.scdn.co/image/6a26104dace4474d27aa8dfd42538b5f55771388","https://i.scdn.co/image/b1131eea51ba4cfebe0e8a86527545372e1b422d","https://i.scdn.co/image/285824e1164d6d597298ff71dedf9c2cd61271bf","https://i.scdn.co/image/14a1459b670d69f9c81224a8837f1ef730748925","https://i.scdn.co/image/78193691f53c3064f09af94f785965629a420410","https://i.scdn.co/image/ec5097e80f63b5056d82f70ee7b28c8ac2b90a74","https://i.scdn.co/image/4b2d7dffb918a5466f9b971a29678f61b0042f75","https://i.scdn.co/image/8b74ba6f8404696b2bcd3e1f0bbb667bd3ac0bd1","https://i.scdn.co/image/8ba0ba7a5af44c4d22c21ce5fbf4d1cbdd824e1d","https://i.scdn.co/image/643467c3c5271d24d3255e95809c2034394b6832","https://i.scdn.co/image/8bfb9630323db892c9cee4ac88919a7e2949597f","https://i.scdn.co/image/4a394aa54ea2af48a12767e6369e9e575c2e24b6","https://i.scdn.co/image/6533298104b2bdb262fb427174aaed2c7f85d9eb","https://i.scdn.co/image/c6e4010c85009c6b03cb9a57386e6453a5bac7e2","https://i.scdn.co/image/80b63a71c88d50f2bdd0417f33b889d795acd818","https://i.scdn.co/image/cfebfc91189818068475d0fd3e30e0969a7ce35a","https://i.scdn.co/image/5fc2da92bc6bc69748e4f7ace2f38f2cb45203b4","https://i.scdn.co/image/54a2f3c9230166bdb4f5334436aa115d9814e45c","https://i.scdn.co/image/e4ffb2f0a62cdb4cade6b537f2a63f47783ac548","https://i.scdn.co/image/0e1c05bab17cb9aede5450e6ebe8e6f30de773b1","https://i.scdn.co/image/e2773b6cac68d016471f0a9ad864aec374049045","https://i.scdn.co/image/ea66d9fe44a46e268972609ae68372c290f0651d","https://i.scdn.co/image/a36ef56c22ecd8e2c8c2fd471392e70df7646cc5","https://i.scdn.co/image/adfa0938e8c6307d979218789ec5e6cf48ae5f89","https://i.scdn.co/image/5d84e5b6ac27c470ce1ff221f8de18a331687fa6","https://i.scdn.co/image/f482a7582501ef509c4fd8f8fdafd6825592bcd8","https://i.scdn.co/image/c6c5d926a50074c2667bb4b3ec8f01156110c149","https://i.scdn.co/image/1ce4819122df5bef668ad6d624d878cb4ecf5b0c","https://i.scdn.co/image/5bc2d85c93dc84a55a19e8f843eda8977a4feb8d","https://i.scdn.co/image/7d3443f568e7f1721532e32844926fb5bfedb2f7","https://i.scdn.co/image/9ddca15e376545668ae0eb0998c5ba3a3a8c1d46","https://i.scdn.co/image/a70dacfe28d41abe6daaeafe2c342ad898201398","https://i.scdn.co/image/37aa1c6bfd3b14fba5eedcf95a509355d166632b","https://i.scdn.co/image/099bff750f13dc8472c685600ed5fd9c82d812c2","https://i.scdn.co/image/361e2e0764713a4902db4aa7afa10e2fccdeead1","https://i.scdn.co/image/0f4205151265c7f640d4bf39fe338841139c89fb","https://i.scdn.co/image/2a502852e21883a791666754c87285af4ee3668e","https://i.scdn.co/image/dad01a2babbf54cc34513d719f5d618b45a2afb4","https://i.scdn.co/image/77eb7c17cafe5503681c33bc806c66ed8e001ec6","https://i.scdn.co/image/0bd8b4864a89b334976c80691dcba328e2a875e6","https://i.scdn.co/image/90577a4014a7e97a2e1f2084d8c331797959aad7","https://i.scdn.co/image/10345b62b24b82c636666de3356fcf1a36920104","https://i.scdn.co/image/556fa69619c281553c7c1c898c889c3aa2174ef2","https://i.scdn.co/image/7678f514a9c5a0d1f870c5eefc0e54ed904d00ba","https://i.scdn.co/image/e836eebcf523b9e6f25f0bd3bc80fbde908c5f78","https://i.scdn.co/image/39aa05d6dce25503b622d1b060c05a632ca0793c","https://i.scdn.co/image/be06e042a8a1fad2d3900852dbbb3b849beae044","https://i.scdn.co/image/ce1b9691b8fbefd6bef33c3a0f1f0a2598cc9e78","https://i.scdn.co/image/e45edae9dd9d3fded77e628cbd107a4d3b53f4d3","https://i.scdn.co/image/158cf5e57eba9aa58b1d050b448465c027c12c25","https://i.scdn.co/image/cbab9c59028ca5772d20780e5d0c3cc974f881fc","https://i.scdn.co/image/205b24447989da3ab34efaa56af5fb1bd70a909e","https://i.scdn.co/image/ea5cf59b2de500c414867841ed48f428485f296d","https://i.scdn.co/image/074a19ab041079a0d1600be7ae3adc40bc651f4f","https://i.scdn.co/image/a6fb9265574606be377a8e1bdad3e7d037e10d35","https://i.scdn.co/image/fe1a549dae2ce99c3492d4d0839c53c390a60866","https://i.scdn.co/image/dfc5ff8174f446a4f94ff0ff6f8e45d8961e2eae","https://i.scdn.co/image/6a866a21c6530965745b618f0d8dc845cce74ee0","https://i.scdn.co/image/2ef7703568ad458b13d6c23f2bea8db0439fa910","https://i.scdn.co/image/f1108e94b4ffda9408ae0ecd226ac74384832e64","https://i.scdn.co/image/6060b439825fc5e070662f103d4d3045a31281ae","https://i.scdn.co/image/5f3806f350594c58369f33d79ad65f7459d47559","https://i.scdn.co/image/ec3a5858cbf3a518915f40fb81c481903c478050","https://i.scdn.co/image/f33fd6f70424009d9576c9b4eb782811d169ea1b","https://i.scdn.co/image/b956302112199d29fded644909d8f67f31b12cd9","https://i.scdn.co/image/ecbee41aa52f8651f68716cf7438e87d9844b985","https://i.scdn.co/image/9730cb9b769dc7f7a46b13a5c9e94c55b9329c67","https://i.scdn.co/image/5701b15f6da1963a63c2c1e71a215b836869a00b","https://i.scdn.co/image/f970fd570f9462d7dbd231e97bd83079881769b0","https://i.scdn.co/image/8de9f794e4afb312155301b38ea13b51f96b6288","https://i.scdn.co/image/4a8b64783e85917be6bd0a7fcb6ba47a5eae3c54","https://i.scdn.co/image/e3e421b3538ca500f8d839102c4308f42ade5421","https://i.scdn.co/image/5f7701f26f2fb27f5834a6a986679f2738d874b1","https://i.scdn.co/image/ffd8d9f6bc64dc1eb98970863bba59ab641a0490","https://i.scdn.co/image/ed05d5d39769250432fce4a52c77793451dd7a71","https://i.scdn.co/image/2e3aa58479d5288463e45fee6f297f5c4c7a57b3","https://i.scdn.co/image/4921f89aa38925eefd252479dca9d482dc102277","https://i.scdn.co/image/f99b1e38c36c9b261be53ed77389e3ab66eb151c","https://i.scdn.co/image/b39ec4ecb2dc7753f59a2167d8905ee55cab2a4e","https://i.scdn.co/image/5949a58104528bd7b372d0154855ff75393a333f","https://i.scdn.co/image/90caef35c2b6d64c7b247c9e6247aa6fd032d151","https://i.scdn.co/image/327e2d05004fccb955c166f3d3f36515abda8fb7","https://i.scdn.co/image/2d3fdec97aa479d229b3a69130a4a3fb0078cfef","https://i.scdn.co/image/00e41dfdaa4119494aa6eb6d0d3aa1b6c08dc625","https://i.scdn.co/image/b8cd256d094a718b86b45c4ec4861e492a167f0e","https://i.scdn.co/image/6435c04eeef8ff60e2a9445dadc70eb1cc1590e7","https://i.scdn.co/image/48333f34338433603bca576ba1b22981d77778a3","https://i.scdn.co/image/022e7f5dd8ddff863f9121ac8e3c8fb1a295afbb","https://i.scdn.co/image/d7ee2872e5da561833c70bcd091eb639b87cfbc6","https://i.scdn.co/image/eaf1e74781d4493e567c17ec9b59d0bc5fe8ba1f","https://i.scdn.co/image/90e339ec7d4dee5e0c85fc0fb0334063e645ff01"]

# jazz = db.current_albums.find({"items.album.genres":"Jazz"})
all_albums = db.current_albums.find()

i = 1
for album in all_albums:
	
	try:
		# urllist = ["https://i.scdn.co/image/2484cbce6034b5a4f5dcdefe9396f3e51c8f905c","https://i.scdn.co/image/8fcb00e9598d7bc9484c163110892e759505cd44","https://i.scdn.co/image/2e8f33da249a6a24fa3569427575217365c156c0","https://i.scdn.co/image/7743bfccf903207bcc7df7b690d5535181c26f7d","https://i.scdn.co/image/c91bcb1b2217354baccc50aada82c76a4568cb83","https://i.scdn.co/image/d285d844d1411f910c1693f05867e7a1c32b22f1","https://i.scdn.co/image/69bb2f1b780964ad3789bdf6cd6de56b41e1c905","https://i.scdn.co/image/756c580ba4b55320c5004957ac2dc8d6970dfb40","https://i.scdn.co/image/9e61413a543b139d663c03838c65bf065fe03e9d","https://i.scdn.co/image/cede55447842b45b233158e6f7d2625c04d2d782","https://i.scdn.co/image/a1d0f7cfc68ee2159b2857de50039ce942678a52","https://i.scdn.co/image/4ca6185e9189a47c164044403b17a1803cba25ff","https://i.scdn.co/image/77eb7c17cafe5503a8484101e5ea2e8f937e1826","https://i.scdn.co/image/6e7cf2fe33c3fcacfbfa11db0088389d05794c76","https://i.scdn.co/image/9474837f9703fede3da3045059d8b33f062b1ce7","https://i.scdn.co/image/2098a9286b1057e1ac79f0e3693c9f316c203ade","https://i.scdn.co/image/d4e2d5cd8330112f67b61f37d747ba8a2bf9412c","https://i.scdn.co/image/fd1a62c7d654c5f048a47f12211ff62f90ed5a8f","https://i.scdn.co/image/920b5d37b9c4e1f2ea2ef8305347e10541caa5a7","https://i.scdn.co/image/ff791466a59f5505fa94e2404b7a679a64ee6496","https://i.scdn.co/image/db9c610bf304c8d22c11bca66db9479d566c3679","https://i.scdn.co/image/7f3afc1788cc8f842dc73f247c2a1078813f367b","https://i.scdn.co/image/abccbaf0dc9ab5e5437e68e40da7abbaba29c93c","https://i.scdn.co/image/57555ff872b3fafde75f8c0d8aa714b538778a6c","https://i.scdn.co/image/77eb7c17cafe5503c3efe7454f721ceece7b2fbb","https://i.scdn.co/image/6301845ad60db4a8cfc9740d7f79a19221309c40","https://i.scdn.co/image/bd8c592720a4f259dc95da52d26778b316103929","https://i.scdn.co/image/33d477d4b01beaef131424bf33182f24bdcef402","https://i.scdn.co/image/6a26104dace4474d27aa8dfd42538b5f55771388","https://i.scdn.co/image/b1131eea51ba4cfebe0e8a86527545372e1b422d","https://i.scdn.co/image/285824e1164d6d597298ff71dedf9c2cd61271bf","https://i.scdn.co/image/14a1459b670d69f9c81224a8837f1ef730748925","https://i.scdn.co/image/78193691f53c3064f09af94f785965629a420410","https://i.scdn.co/image/ec5097e80f63b5056d82f70ee7b28c8ac2b90a74","https://i.scdn.co/image/4b2d7dffb918a5466f9b971a29678f61b0042f75","https://i.scdn.co/image/8b74ba6f8404696b2bcd3e1f0bbb667bd3ac0bd1","https://i.scdn.co/image/8ba0ba7a5af44c4d22c21ce5fbf4d1cbdd824e1d","https://i.scdn.co/image/643467c3c5271d24d3255e95809c2034394b6832","https://i.scdn.co/image/8bfb9630323db892c9cee4ac88919a7e2949597f","https://i.scdn.co/image/4a394aa54ea2af48a12767e6369e9e575c2e24b6","https://i.scdn.co/image/6533298104b2bdb262fb427174aaed2c7f85d9eb","https://i.scdn.co/image/c6e4010c85009c6b03cb9a57386e6453a5bac7e2","https://i.scdn.co/image/80b63a71c88d50f2bdd0417f33b889d795acd818","https://i.scdn.co/image/cfebfc91189818068475d0fd3e30e0969a7ce35a","https://i.scdn.co/image/5fc2da92bc6bc69748e4f7ace2f38f2cb45203b4","https://i.scdn.co/image/54a2f3c9230166bdb4f5334436aa115d9814e45c","https://i.scdn.co/image/e4ffb2f0a62cdb4cade6b537f2a63f47783ac548","https://i.scdn.co/image/0e1c05bab17cb9aede5450e6ebe8e6f30de773b1","https://i.scdn.co/image/e2773b6cac68d016471f0a9ad864aec374049045","https://i.scdn.co/image/ea66d9fe44a46e268972609ae68372c290f0651d","https://i.scdn.co/image/a36ef56c22ecd8e2c8c2fd471392e70df7646cc5","https://i.scdn.co/image/adfa0938e8c6307d979218789ec5e6cf48ae5f89","https://i.scdn.co/image/5d84e5b6ac27c470ce1ff221f8de18a331687fa6","https://i.scdn.co/image/f482a7582501ef509c4fd8f8fdafd6825592bcd8","https://i.scdn.co/image/c6c5d926a50074c2667bb4b3ec8f01156110c149","https://i.scdn.co/image/1ce4819122df5bef668ad6d624d878cb4ecf5b0c","https://i.scdn.co/image/5bc2d85c93dc84a55a19e8f843eda8977a4feb8d","https://i.scdn.co/image/7d3443f568e7f1721532e32844926fb5bfedb2f7","https://i.scdn.co/image/9ddca15e376545668ae0eb0998c5ba3a3a8c1d46","https://i.scdn.co/image/a70dacfe28d41abe6daaeafe2c342ad898201398","https://i.scdn.co/image/37aa1c6bfd3b14fba5eedcf95a509355d166632b","https://i.scdn.co/image/099bff750f13dc8472c685600ed5fd9c82d812c2","https://i.scdn.co/image/361e2e0764713a4902db4aa7afa10e2fccdeead1","https://i.scdn.co/image/0f4205151265c7f640d4bf39fe338841139c89fb","https://i.scdn.co/image/2a502852e21883a791666754c87285af4ee3668e","https://i.scdn.co/image/dad01a2babbf54cc34513d719f5d618b45a2afb4","https://i.scdn.co/image/77eb7c17cafe5503681c33bc806c66ed8e001ec6","https://i.scdn.co/image/0bd8b4864a89b334976c80691dcba328e2a875e6","https://i.scdn.co/image/90577a4014a7e97a2e1f2084d8c331797959aad7","https://i.scdn.co/image/10345b62b24b82c636666de3356fcf1a36920104","https://i.scdn.co/image/556fa69619c281553c7c1c898c889c3aa2174ef2","https://i.scdn.co/image/7678f514a9c5a0d1f870c5eefc0e54ed904d00ba","https://i.scdn.co/image/e836eebcf523b9e6f25f0bd3bc80fbde908c5f78","https://i.scdn.co/image/39aa05d6dce25503b622d1b060c05a632ca0793c","https://i.scdn.co/image/be06e042a8a1fad2d3900852dbbb3b849beae044","https://i.scdn.co/image/ce1b9691b8fbefd6bef33c3a0f1f0a2598cc9e78","https://i.scdn.co/image/e45edae9dd9d3fded77e628cbd107a4d3b53f4d3","https://i.scdn.co/image/158cf5e57eba9aa58b1d050b448465c027c12c25","https://i.scdn.co/image/cbab9c59028ca5772d20780e5d0c3cc974f881fc","https://i.scdn.co/image/205b24447989da3ab34efaa56af5fb1bd70a909e","https://i.scdn.co/image/ea5cf59b2de500c414867841ed48f428485f296d","https://i.scdn.co/image/074a19ab041079a0d1600be7ae3adc40bc651f4f","https://i.scdn.co/image/a6fb9265574606be377a8e1bdad3e7d037e10d35","https://i.scdn.co/image/fe1a549dae2ce99c3492d4d0839c53c390a60866","https://i.scdn.co/image/dfc5ff8174f446a4f94ff0ff6f8e45d8961e2eae","https://i.scdn.co/image/6a866a21c6530965745b618f0d8dc845cce74ee0","https://i.scdn.co/image/2ef7703568ad458b13d6c23f2bea8db0439fa910","https://i.scdn.co/image/f1108e94b4ffda9408ae0ecd226ac74384832e64","https://i.scdn.co/image/6060b439825fc5e070662f103d4d3045a31281ae","https://i.scdn.co/image/5f3806f350594c58369f33d79ad65f7459d47559","https://i.scdn.co/image/ec3a5858cbf3a518915f40fb81c481903c478050","https://i.scdn.co/image/f33fd6f70424009d9576c9b4eb782811d169ea1b","https://i.scdn.co/image/b956302112199d29fded644909d8f67f31b12cd9","https://i.scdn.co/image/ecbee41aa52f8651f68716cf7438e87d9844b985","https://i.scdn.co/image/9730cb9b769dc7f7a46b13a5c9e94c55b9329c67","https://i.scdn.co/image/5701b15f6da1963a63c2c1e71a215b836869a00b","https://i.scdn.co/image/f970fd570f9462d7dbd231e97bd83079881769b0","https://i.scdn.co/image/8de9f794e4afb312155301b38ea13b51f96b6288","https://i.scdn.co/image/4a8b64783e85917be6bd0a7fcb6ba47a5eae3c54","https://i.scdn.co/image/e3e421b3538ca500f8d839102c4308f42ade5421","https://i.scdn.co/image/5f7701f26f2fb27f5834a6a986679f2738d874b1","https://i.scdn.co/image/ffd8d9f6bc64dc1eb98970863bba59ab641a0490","https://i.scdn.co/image/ed05d5d39769250432fce4a52c77793451dd7a71","https://i.scdn.co/image/2e3aa58479d5288463e45fee6f297f5c4c7a57b3","https://i.scdn.co/image/4921f89aa38925eefd252479dca9d482dc102277","https://i.scdn.co/image/f99b1e38c36c9b261be53ed77389e3ab66eb151c","https://i.scdn.co/image/b39ec4ecb2dc7753f59a2167d8905ee55cab2a4e","https://i.scdn.co/image/5949a58104528bd7b372d0154855ff75393a333f","https://i.scdn.co/image/90caef35c2b6d64c7b247c9e6247aa6fd032d151","https://i.scdn.co/image/327e2d05004fccb955c166f3d3f36515abda8fb7","https://i.scdn.co/image/2d3fdec97aa479d229b3a69130a4a3fb0078cfef","https://i.scdn.co/image/00e41dfdaa4119494aa6eb6d0d3aa1b6c08dc625","https://i.scdn.co/image/b8cd256d094a718b86b45c4ec4861e492a167f0e","https://i.scdn.co/image/6435c04eeef8ff60e2a9445dadc70eb1cc1590e7","https://i.scdn.co/image/48333f34338433603bca576ba1b22981d77778a3","https://i.scdn.co/image/022e7f5dd8ddff863f9121ac8e3c8fb1a295afbb","https://i.scdn.co/image/d7ee2872e5da561833c70bcd091eb639b87cfbc6","https://i.scdn.co/image/eaf1e74781d4493e567c17ec9b59d0bc5fe8ba1f","https://i.scdn.co/image/90e339ec7d4dee5e0c85fc0fb0334063e645ff01"]
		url = album["items"]["album"]["images"][0]["url"]
		album_id = album["items"]["album"]["id"]
		filename = str(url)+".jpg"
		# save_path = '../data/images/'
		# completeName = os.path.join(save_path, filename)
		file = album_id
		urllib.request.urlretrieve(url,file)
		# os.rename(file, "../data/images/"+file)
		shutil.move(file, "../data/images/"+file)
		# j = str(i)+'/'+str(len(jazz))
		# i+=1
		i+=1
		denom = '/'+str(all_albums.count())
		stdout.write("\r%d" % i +denom)
		# stdout.write('/'+str(a*b))
		stdout.flush()
	except Exception:
		i+=1
		print(str(i)+" doesn't work.")
	


