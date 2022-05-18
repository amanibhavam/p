VERSION --parallel-load --shell-out-anywhere --use-chmod --use-host-command 0.6
# --use-registry-for-with-docker

IMPORT github.com/defn/cloud/lib:master AS lib

FROM lib+platform

ARG stack

main:
    COPY main.py .
    SAVE ARTIFACT main.py

fit:
    FROM lib+fit --stack=${stack} --target=github.com/katt-org/p+main

debug:
    FROM +fit
    RUN --no-cache find .terraform.d/plugin-cache .terraform/providers -ls