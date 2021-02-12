* Review cloning RS2
* Run DesignAnalyzer
* Talk about how to get rid of compile errors by deleting
* Before installing Tincr let's run some more...
    * Talk about how to do referencedLibraries
    * Talk about javadocs
* Run DesignAnalyzer on add.rscp
    * Show how to set run/debug configurations
        * Start with Run->Open Configurations, see all the auto-generated ones
        * Now, look at debug icon (left side), pull-down, Settings, Run triangle
    * Add "args" to DesignAnalyzer: "args": ["/home/nelson/exampleVivadoDesigns/add.rscp"]
        * Don't forget the preceding comma since this is a list (is `launch.json` file)
    * Now, run
* Generate own .rscp
    * Note that add.rscp is unplaced
    * Go into `exampleVivadoDesigns` and show what is there
    * Open up `compile.tcl` and talk about it
        * Note the `package require tincr`
    * Back to installing Tincr
    * Back to `compile.tcl`
        * Note how the routine expects a certain directory structure
        * Note how the routine will generate a .rscp as well as .dcp
        * Note how the routine doesn't place or route
            * Fix that and re-run
* Talk about how the VS Code terminal gets icky - reset it with `exit`
* Generate a `count3.rscp`
    * Edit run config
    * Run `DesignAnalyzer` with it, look at output
* Run `DotFilePrinterDemo` and see what gets generated for add.
    * Install `graphviz`
    * Do preview (which works because I installed `graphviz`)
* Go look at javadocs and wander around `.../subsite` and `CellDesign` and `Cell`
* Go look through `DesignAnalyzer`, `DeviceAnalyzer`, `CreateDesignExample`, `ImportExportExample`.
* Talk about `.rscp` and `.tcp` files




