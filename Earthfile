VERSION --shell-out-anywhere --use-chmod --use-host-command --earthly-version-arg --use-copy-link 0.6

IMPORT github.com/defn/cloud/lib:master AS lib

ARG target=github.com/katt-org/p+warm
ARG stack

warm:
    FROM lib+platform
    COPY poetry.lock pyproject.toml
    RUN poetry install
    COPY foo foo
    COPY main.py .
    SAVE ARTIFACT foo

update:
    FROM lib+init --target=${target} --stack=${stack}
    SAVE ARTIFACT poetry.lock AS LOCAL poetry.lock
    SAVE ARTIFACT pyproject.toml poetry.lock AS LOCAL pyproject.toml

plan:
    FROM lib+plan --target=${target} --stack=${stack}
    SAVE ARTIFACT cdktf.out AS LOCAL cdktf.out
    SAVE ARTIFACT poetry.lock AS LOCAL poetry.lock
    SAVE ARTIFACT pyproject.toml AS LOCAL pyproject.toml

apply:
    FROM lib+apply --target=${target} --stack=${stack}
