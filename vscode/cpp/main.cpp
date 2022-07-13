#include <iostream>
#include <fstream>
#include <vector>
#include "item.h"
int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        return 1;
    }
    std::ifstream input(argv[1]);
    std::ofstream output("output.txt");
    std::string line;
    std::vector<Item *> items;
    std::vector<Item *> produce;
    std::vector<Item *> grains;
    if (input.is_open())
    {
        while (getline(input, line))
        {
            Item *item = Item::parseItem(line);
            items.push_back(item);
            if (item->getType() == Item::PRODUCE)
            {
                produce.push_back(item);
            }
            else
            {
                grains.push_back(item);
            }
        }
        input.close();
    }
    output.precision(2);
    output << std::fixed;
    output << "All Items:" << std::endl;
    float totalCost = 0;
    for (Item *item : items)
    {
        output << item->toString() << std::endl;
        totalCost += item->getTotalCost();
    }
    output << "Total $" << totalCost << std::endl
           << std::endl;
    output << "Grains:" << std::endl;
    totalCost = 0;
    for (Item *item : grains)
    {
        output << item->toString() << std::endl;
        totalCost += item->getTotalCost();
    }
    output << "Total $" << totalCost << std::endl
           << std::endl;

    output << "Produce:" << std::endl;
    totalCost = 0;
    for (Item *item : produce)
    {
        output << item->toString() << std::endl;
        totalCost += item->getTotalCost();
    }
    output << "Total $" << totalCost << std::endl
           << std::endl;
}
