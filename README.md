# files-dbt-redshift

Meltano project [file bundle](https://meltano.com/docs/command-line-interface.html#file-bundle) for [dbt](https://www.getdbt.com/).

Files:
- [`transform/models`](./bundle/transform/models) (directory)
- [`transform/profile/profiles.yml`](./bundle/transform/profiles/redshift/profiles.yml)
- [`transform/dbt_project.yml`](./bundle/transform/dbt_project.yml)
- [`transform/.gitignore`](./bundle/transform/.gitignore)

```py
# Add dbt-redshift transformer and this file bundle to your Meltano project
meltano add transformer dbt-redshift

# Add only this file bundle to your Meltano project
meltano add files dbt-redshift
```
