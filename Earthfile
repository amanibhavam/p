VERSION --shell-out-anywhere --use-chmod --use-host-command --earthly-version-arg --use-copy-link 0.6

IMPORT github.com/defn/cloud/lib:master AS lib

FROM lib+platform

ARG stack

warm:
    COPY pyproject.toml poetry.lock .
    RUN ~/bin/e poetry install
    COPY main.py .
    SAVE ARTIFACT main.py

update:
    FROM +warm
    RUN ~/bin/e poetry update
    SAVE ARTIFACT poetry.lock AS LOCAL poetry.lock

plan:
    FROM lib+plan --stack=${stack} --target=github.com/katt-org/p+warm

apply:
    FROM lib+apply --stack=${stack} --target=github.com/katt-org/p+warm
