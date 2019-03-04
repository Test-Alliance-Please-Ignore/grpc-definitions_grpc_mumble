from setuptools import setup


setup(
    name="grpc_mumble",
    version="0.1.0",
    packages=["grpc_mumble"],
    install_requires=["grpcio", "googleapis-common-protos"],
    zip_safe=False,
)
