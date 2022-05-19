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
    FROM lib+warm --target=github.com/katt-org/p+warm
    RUN ~/bin/e poetry update
    SAVE ARTIFACT poetry.lock AS LOCAL poetry.lock

plan:
    FROM lib+plan --target=github.com/katt-org/p+warm --stack=${stack}

apply:
    FROM lib+apply --target=github.com/katt-org/p+warm --stack=${stack}
