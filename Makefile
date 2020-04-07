
COMMONS = $(patsubst %/,%,$(dir $(wildcard */Makefile)))
_PORTS = $(wildcard ports/*)
PORTS = $(notdir $(_PORTS))


.PHONY: $(COMMONS) $(_PORTS) $(PORTS)
.SECONDARY: $(_PORTS)


$(PORTS): mpy-cross
	@$(MAKE) ports/$@

$(_PORTS) $(COMMONS):
	$(MAKE) -C $@ $(SUB)

clean:
	$(MAKE) -k $(COMMONS) $(_PORTS) SUB=clean
	$(MAKE) -C mpy-cross clean


define PORT_template =
_$(1)_TARGETS = $$(shell grep -oP '^[a-z\d _-]+(?=:)' ports/$(1)/Makefile)
$(1)_TARGETS = $$(addprefix $(1)-,$$(_$(1)_TARGETS))

$$($(1)_TARGETS):

$(1)-%:
	$$(MAKE) ports/$(1) SUB=$$*

$(1)-install-modules: unix
ifeq ($$(MODS),)
	$$(error Modules to be installed not defined. Set MODS="<mod> ...")
endif
	ports/unix/micropython -m upip install -p ports/$(1)/modules $$(MODS)
endef

$(foreach port,$(PORTS),$(eval $(call PORT_template,$(port))))

