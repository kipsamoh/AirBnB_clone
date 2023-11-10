#!/usr/bin/env bash

set -e

# Get the directory of the script
SCRIPTDIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# Get the root directory (parent directory of the script)
ROOTDIR="$(cd "${SCRIPTDIR}/.." && pwd)"

# Change to the Git repository directory
cd "${ROOTDIR}/AirBnB_clone"

# Continue script execution even if some commands fail
set -x

# Generate AUTHORS file, placing kipsamoh <kipsamoh@gmail.com> as the first contributor
cat > "${ROOTDIR}/AirBnB_clone/AUTHORS" <<- EOF
    # This file lists all contributors to the repository.

    $(git log --format='%aN <%aE>' | grep -v -E '^(kipsamoh <133492659\+kipsamoh@users\.noreply\.github\.com>|kipsamoh <kipsamoh@gmail\.com>)$' | LC_ALL=C.UTF-8 sort -uf | sed 's/ /_/g')
    Daniel Chebet <kipsamoh@gmail.com>
EOF
