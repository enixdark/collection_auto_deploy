help:
	@echo "  generate    generate yaml file"
	@echo "  clean       remove yaml files"
	@echo "  run         create pvc, pv, rc, svc, pod"

generate:
	@python setup.py generate

clean:
	@python setup.py clean

run:
	@for f in mysql/*.yaml postgres/*.yaml kong/*.yaml ; do echo "$f" ; done

