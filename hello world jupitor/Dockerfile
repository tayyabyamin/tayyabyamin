FROM python:3.12
WORKDIR /workspace
COPY hello_world.ipynb .
RUN pip install notebook
EXPOSE 8888
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root", "--no-browser"]
