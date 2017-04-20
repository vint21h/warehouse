# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import alembic.command
import click

from warehouse.cli.db import db, alembic_lock


@db.command()
@click.argument("revision", required=True)
@click.pass_obj
def show(config, revision, **kwargs):
    """
    Show the revision(s) denoted by the given symbol.
    """
    with alembic_lock(config.registry["sqlalchemy.engine"],
                      config.alembic_config()) as alembic_config:
        alembic.command.show(alembic_config, revision, **kwargs)
