#include "item.h"
#include "grain.h"
#include "produce.h"
Item *Item::parseItem(std::string line)
{
    Item *item;
    std::string type = extractNextAttribute(line);
    if (type == "grian")
    {
        item = new Grain(line);
    }
    else
    {
        item = new Produce(line);
    }
    return item;
}