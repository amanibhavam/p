VERSION --shell-out-anywhere --use-chmod --use-host-command --earthly-version-arg --use-copy-link 0.6

IMPORT github.com/defn/cloud/lib:master AS lib

ARG target=github.com/katt-org/p+warm
ARG stack

warm:
    FROM lib+platform
    COPY main.py .
    SAVE ARTIFACT main.py

plan:
    FROM lib+plan --target=${target} --stack=${stack}
    SAVE ARTIFACT cdktf.out AS LOCAL cdktf.out

apply:
    FROM lib+apply --target=${target} --stack=${stack}
    SAVE ARTIFACT cdktf.out AS LOCAL cdktf.out
