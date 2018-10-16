font = Glyphs.font
import math
import re

# Sync everything to cubic NLI layer

currentGlyph = Glyphs.font.selectedLayers[0].parent

def getFullName(layerName):
	for layer in currentGlyph.layers:
		if re.match(layerName + ".*}$", layer.name):
			return layer.name


def syncToNLI(aName, cName, dName, bName, NLIName):	
	currentGlyph = Glyphs.font.selectedLayers[0].parent
	
	c2Name = getFullName(re.sub("\d", "2", cName))
	c3Name = getFullName(re.sub("\d", "3", cName))
	cName = getFullName(cName)
	
	d2Name = getFullName(re.sub("\d", "2", dName))
	d3Name = getFullName(re.sub("\d", "3", dName))
	dName = getFullName(dName)
	bName = getFullName(bName)

	for node in currentGlyph.layers[0].paths[0].nodes:	
		currentGlyph.layers[aName].paths[0].nodes[node.index].position = currentGlyph.layers[NLIName].paths[node.index].nodes[0].position
		
		currentGlyph.layers[cName].paths[0].nodes[node.index].position = currentGlyph.layers[NLIName].paths[node.index].nodes[1].position
		currentGlyph.layers[c2Name].paths[0].nodes[node.index].position = currentGlyph.layers[NLIName].paths[node.index].nodes[1].position
		currentGlyph.layers[c3Name].paths[0].nodes[node.index].position = currentGlyph.layers[NLIName].paths[node.index].nodes[1].position
		
		currentGlyph.layers[dName].paths[0].nodes[node.index].position = currentGlyph.layers[NLIName].paths[node.index].nodes[2].position
		currentGlyph.layers[d2Name].paths[0].nodes[node.index].position = currentGlyph.layers[NLIName].paths[node.index].nodes[2].position
		currentGlyph.layers[d3Name].paths[0].nodes[node.index].position = currentGlyph.layers[NLIName].paths[node.index].nodes[2].position
		
		currentGlyph.layers[bName].paths[0].nodes[node.index].position = currentGlyph.layers[NLIName].paths[node.index].nodes[3].position


syncToNLI("Regular", "C1", "D1", "B", "B NLI")
syncToNLI("Regular Oblique", "E1", "F1", "G", "G NLI")
syncToNLI("Bold", "H1", "I1", "J", "J NLI")
syncToNLI("Bold Oblique", "K1", "L1", "M", "M NLI")